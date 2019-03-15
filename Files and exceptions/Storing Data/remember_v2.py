
import json

def get_stored_username():

    filename = 'username_v2.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, "+username+"!")
    else:
        username = input("What's your name? ")
        filename = 'username_v2.json'
        with open(filename,'w') as f_obj:
            json.dump(filename,f_obj)
            print("We'll remeber you when you come back, "+username+"!")
        
greet_user()
