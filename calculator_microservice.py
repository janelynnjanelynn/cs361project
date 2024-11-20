import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #Receive and open message from main program.
    message = socket.recv()
    print(f"Received request from the client:{message.decode()}.")
    if len(message) > 0:
        if message.decode() == 'WAIT':
            break
        #Format string into floats and run calculations; create two lists of floats, one for each income/expenses.
        yeet_string = message.decode()
        income_total = 0
        expense_total = 0
        splitty = yeet_string.split(";")

        income_split = []
        expense_split = []
        for count_elem in range(len(splitty)):
            splitty[count_elem] = splitty[count_elem].strip()[1:len(splitty[count_elem])-1]
            listy = splitty[count_elem].split(",")
            if count_elem == 0:
                income_split = listy
            else:
                expense_split = listy
        income_float = []
        for item in income_split:
            income_float.append(float(item.strip()))
        expense_float = []
        for item in expense_split:
            expense_float.append(float(item.strip()))

        #Calculate income, expenses, net income, and determine message to return to main program.
        user_income = 0
        user_expenses = 0
        for num in income_float:
            user_income += num
        for num in expense_float:
            user_expenses += num
        if user_expenses > 0:
            user_expenses = user_expenses * (-1)
        user_netincome = user_income + user_expenses

        net_message = ""
        if user_netincome > 0:
            net_message = "Well done! We are in the positive!"
        elif user_netincome == 0:
            net_message = "Seems you broke even!"
        else:
            net_message = "OOF, it appears we are in the negative!"

        #Create string to send back to main program and send it.
        return_string = (f"Total Income: {user_income:.2f}\nTotal Expenses: {user_expenses:.2f}\nNet Income: {user_netincome:.2f}\n{net_message}")
        time.sleep(3)
        socket.send_string(return_string)
        print(f"Sending the following message: \n{return_string}")
context.destroy()