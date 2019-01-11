
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("\nEnd loop")


requested_tooping = 'mushrooms'

if requested_tooping != 'anchovies':
    print("Hold the anchovies!\n")


#checking whether a value is not in a list

banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title()+", you can post a response if you wish.\n")

car = 'subaru'
print(car == 'subaru')


string1 = "hola"
string2 = "mundo"

if string1 == string2:
    print(":)\n")
else:
    print(":(\n"+string1.upper())

print("who are you")
#name = input()
#print("Hello .. :) "+name.title())

age = 12

if age < 4:
    print("Your admission cost is $60")
elif age < 18:
    print("Your admission cost is %5.")
else:
    print("Your admission cost is $10.")

requested_s = ['mushrooms','green peppers','extra cheese']

for requested in requested_s:
    if requested == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding "+ requested+".")
print("\nFinished making your pizza!")

print("-----------\n")
new_list = []

if new_list:
    for i in new_list:
        print("Adding "+i+".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")