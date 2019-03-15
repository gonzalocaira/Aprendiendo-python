
import json

def get_favorite_number():
    filename = 'favorite_number.json'
    #usernumber = input("Write a favorite number: ") #error
    try:
        with open(filename) as f_obj:
            usernumber = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return usernumber

def new_number():
    usernumber = input("What's is you favorite number? ")
    filename = 'favorite_number.json'
    with open(filename,'w') as f_obj:
        json.dump(usernumber,f_obj)
    return usernumber

def you_favorite_number():
    usernumber = get_favorite_number()
    if usernumber:
        print("I know your favorite number is "+usernumber)
    else:
        #new favorite number
        usernumber = new_number()
        print("We'll remember you when you come back, "+usernumber +"!")


you_favorite_number()       