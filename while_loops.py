
#the while loopin action
"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit to end the program. "

message = ""
#while message != 'quit':
    #message = input(prompt)
    #print(message)

# USING A FLAG

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit to end the program. "

active = True
#while active:
 #   message = input(prompt)
  #  if message == 'quit':
  #      active = False
  #  else:
   #     print(message)


#Using break to exit a loop"""
"""
prompt = "\nPlease enter the name of a city have visited: "
prompt += "\nEnter 'quit' when you are finished. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")"""
"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)"""

responses = {}

#set a flag  to indicate that polling is active
polling_active = True

while polling_active:
    #prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #Store the response in the dictionary:
    responses[name] = response

    #find out if anyone else is goin to take the poll.
    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False
#polling is complete. Show the results
print("\n--- Poll Results ---")
for name, reponse in responses.items():
    print(name + "would like to climb" +  response +".")
    