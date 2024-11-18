import sys
import json

def welcome_page():
    while True:
        welcome_prompt = ("""\nWelcome to the Yummy Recipes application! We are happy to have you!\nSave your favorite recipes in your own personal catalog.\nEnter "x" or "quit" to close the application at any time.\nEnter 5 for more information, enter 2 to create an account, or enter 1 to log in: """)
        welcome_input = input(welcome_prompt)
        if welcome_input == "5":
            more_information()
        elif welcome_input == "2":
            username = "example"
            pin = "1234"
            confirmation = "not confirmed"
            username, pin, confirmation = create_account(username, pin, confirmation)
            if confirmation == "":
                backend_create_account(username, pin)
                login_welcome(username)
        elif welcome_input == "1":
            username = "example"
            pin = "1234"
            username, pin = user_login(username, pin)
            login_welcome(username)
        elif welcome_input == "x":
            quit_app()
        elif welcome_input == "quit":
            quit_app()
        else:
            print("""\nSorry, we didn't quite catch that. Please try again.\n""")

def more_information():
    while True:
        information_details = ("""\nYummy Recipes: more information!\nThe Yummy Recipes application was created for users to save recipes that they like or may be interested in.\nAfter creating an account, users can manually enter recipes, including titles, ingredients, and step by step instructions.\nUsers are also able to favorite the extra delicious recipes and mark recipes that they have cooked.\nIn turn, users are able to view their saved recipes, cooked recipes, and favorite recipes.\nNever lose yummy recipes again!\nEnter "x" or "quit" to close the application at any time.\nWhen you are done reading, enter 9 to return to the welcome screen: """)
        exit_more_information = input(information_details)
        if exit_more_information == "x":
            quit_app()
        if exit_more_information == "quit":
            quit_app()
        if exit_more_information != "9":
            print("\nSorry, we didn't quite catch that. Please try again.")
        else:
            break
    return

def app_functions():
    while True:
        information_details = ("""\nPlease see below for more information on each functionality.\nWe aim to curate a personalized cooking experience.\nEnter "9" to return to the previous page\nEnter "x" or "quit" on any page to log out.\n""")
        exit_more_information = input(information_details)
        if exit_more_information == "9":
            break
        elif exit_more_information == "x":
            quit_app()
        elif exit_more_information == "quit":
            quit_app()
        else:
            print("\nSorry, we didn't quite catch that. Please try again.")
    return

def create_account(username, pin, confirmation):
    create_prompt = ("""\nTo create an account, you will need to enter a username and a 4-digit pin which will serve as your password.\nThese credentials will be used to log in each time.\nIf you would like to proceed with creating an account, please note that you will need to take additional time (1-2 minutes) to come up with a unique username and password.\nIn addition, you will need to memorize or store this username and password combination for use when you return to this application at a later time.\nOnce details are entered, please press enter to continue.""")
    username_prompt = ("""Username: """)
    pin_prompt = ("""Pin: """)
    confirmation_prompt = ("""Are you sure you want to create this account?\nThis is a rookie application, so we cannot promise that your username and password combination will not be leaked.\nTherefore, we recommend that you pick a username and password that you do not use for key accounts.\nPlease proceed with caution if you choose to do so.\nPress ENTER to create this account or type 9 to return to the welcome screen.\n""")
    print(create_prompt)
    username = input(username_prompt)
    pin = input(pin_prompt)
    confirmation = input(confirmation_prompt)
    return username, pin, confirmation

def backend_create_account(username, pin):
    with open('userdetails.json', 'r') as readfile:
        dataload = json.load(readfile)
        dataload[username] = pin
    with open('userdetails.json','w') as writefile:
        json.dump(dataload, writefile)
    return

def user_login(username, pin):
    login_prompt = ("""\nWelcome back! Please enter your username and pin below to log in and access your personal profile. Once details are entered, press ENTER to continue.\n""")
    print(login_prompt)
    while True:
        username_prompt = ("""Username: """)
        pin_prompt = ("""Pin: """)
        username = input(username_prompt)
        pin = input(pin_prompt)
        with open('userdetails.json', 'r') as readfile:
            dataload = json.load(readfile)
            if dataload[username] == pin:
                break
            else:
                print("""Something's not right. Please try again.\n""")
    return username, pin

def login_welcome(username):
    while True:
        welcome_prompt = (f"""\nHello {username}! Let's get started on your personalized cooking journey.\nEnter 5 for more detailed information on the options.\nEnter "logout" to log out.\nEnter "x" or "quit" to exit the program. \n""")
        user_input = input(welcome_prompt)
        if user_input == "5":
            app_functions()
        elif user_input == "logout":
            print("""Logging you out and returning to welcome screen.""")
            break
        elif user_input == "x" or "quit":
            quit_app()
    return

def quit_app():
    sys.exit(1)

welcome_page()
