
magicians = ['alice','david','carolina']

for magician in magicians:
    print(magician)

list_new = ['111111','5','6','9','2']
print(list_new)
list_num= [9,8,3,7,56,63]
print(list_num)
list_new.sort()
print(list_new)
list_num.sort(reverse=1)
list_num.insert(2,0)
list_num.append(4)
print(list_num)

for num in magicians:
    print(num + " that")
    print("was a great trick!"+".\n")
    #print('2\n')

    print ("xd")
    
##WTF!!!
magic = ['alice', 'david', 'carolina']
for magi in magic:
    print(magi.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you everyone, that was a great magic show!")
# does not print last value 1,2,3,4,5  ... not 6
for value in range(1,6):
    print(value)

#using range () to make a list of numbers

numbers = list(range(10,16))
print(numbers)

#more

even_numbers = list(range(2,11,2))
print(even_numbers)

#playing 
# ; ; ;
squares = []
for value in range (1,11):
    #square = value**2;
    squares.append(value**2);

print(squares)

#simple statistics with a list of numbers
#a few Python functions are specific to lists of numbers.

digits = [1,2,3,4,5,6,7,8,9,0]
var_m =min(digits)
print(var_m)
var_max = max(digits)
var_sum = sum(digits)
print(var_max)
print(var_sum)

#working with part of a list

#slicing a list

players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[:2])
print(players[-3:])
players_2 = players [2:]
print(players_2)

print("Here are the first three players on my team")
for player in players[:3]:
        print(player.title())

##Copying a list

my_foods = ['pizza','falafel','carrot cake']
friend_foods =my_foods[:]

#friend_foods = my_foods
#En lugar de almacenar una copia de my_foods en friend_foods 
# en u, establecemos
#friend_foods igual a my_foods. :O!
print("My favorite foods are :")
print(my_foods)

print("\nMy friend's favorite foods are :")
print(friend_foods)


num = [8,1,9,3,7,3,7,3,4,69,2,7,9]
print(num[-3:])

#tuple
dimensions = (200,50)
#print(dimensions[0])
#print(dimensions[1])
print("Original Dimensions:")
for dimension in dimensions:
        print(dimension)

dimensions = (400,100,300)
print("\nModified dimensions:")
for dimension in dimensions:
        print(dimension)

for i in range(10)
    print(i)



