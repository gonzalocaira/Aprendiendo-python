
import json

#numbers = [2,3,5,7,11,13]


# Dump = write in the file 
"""
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
"""
# LOAD
""" 
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
"""
user_name = input("What is your name? ")

filename2 = 'username.json'
#dump
with open(filename2,'w') as f_obj:
    json.dump(user_name,f_obj)
    print("We'll remeber you when you come back, "+user_name+"!")
#load
with open(filename2) as f_obj:
    user_name = json.load(f_obj)
    print("Welcome back, "+user_name+"!")