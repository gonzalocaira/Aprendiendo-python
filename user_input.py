
#Chapter 7

#how the input functions works

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

#writing clear prompts

#name = input("Pleasure enter your name: ")
#print("Hello, "+name+"!")


#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\n What is your first nane? "

#name =input(prompt)

#print("\nHello, "+name+"!")


#CONVERTED

#height = input("How tall are you , in inches? ")
#height = int(height)

#if height >= 36:
#    print("\nYou're tall enough to ride!")
#else:
#    print("\nYou'll be able to ride when you're a little older.")


#THE MODULO OPERATOR

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")
    