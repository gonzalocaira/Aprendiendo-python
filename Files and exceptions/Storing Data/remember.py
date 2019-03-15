
import json

#Load the username, if it has been stored previosly
# Otherwise, prompt for the username and store it.
def greet_user():
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What's your name? ")
        with open(filename) as f_obj:
            json.dump(username,f_obj)
            print("We'll remeber you when you come back, "+username+"!")
    else:
        print("Welcome back, "+username+"!")
greet_user()