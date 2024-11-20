Calculator (Net Difference) Microservice

REQUEST data
To request data from the calculator (net difference) microservice, a string must be sent via ZMQ socket from the main program (client) to the microservice (server). In the main program, this is done by calling socket.send_string(), where the intended string to send is included in the parenthesis. The string sent from the main program to the server should be formatted in an f-string separated by a semi-colon. In the context of calculating someone's net income, the string may be in the format send_string = (f"{income};{expenses}"), where {income} and {expenses} are lists of unsigned numbers. An example string sent to the microservice may be "[1, 2, 3];[1, 2, 3]" where the first set of brackets contains income and the second set of brackets contains expenses.

EXAMPLE REQUEST: Prepare string to send via ZMQ and send it

yeet_string = (f"{income};{expenses}")

socket.send_string(yeet_string)

RECEIVE data
The microservice calculates the minuend, the subtrahend, and the difference, and returns the calculated numbers along with a message depending on whether the difference is positive, negative, or zero. To receive the data, the main program will use socket.recv(). This should be stored in a variable (e.g., message = socket.recv()) which may be decoded with the .decode() function (e.g., socket.recv()). This message can then be displayed to the user on the main program.

EXAMPLE RECEIVE:

message = socket.recv()

print(f"\nReceived the following message:\n{message.decode()}")

UML Diagram below:
![image](https://github.com/user-attachments/assets/8e6dc4c0-6a05-4ba1-9822-70dd451d69f3)
