

#A simple dictionary
alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#working with dictionaries 

#accesing value in a dictionry

print(alien_0['color'])

new_points = alien_0['points']
print("You just earned "+ str(new_points)+ " points!")


alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

alien_dictionarie = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+ str(alien_dictionarie['x_position']))

#move the alien to the right.
#determne how far to move the alien based on its current speed.

if alien_dictionarie['speed'] == 'slow' :
    x_increment = 1
elif alien_dictionarie['speed'] == 'medium' :
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3

#the new position is the old position plus the increment
alien_dictionarie['x_position'] = alien_dictionarie['x_position'] + x_increment
print("New x_position : " + str(alien_dictionarie['x_position']))

#REMOVING Key_value pairs

print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("Sara's favorite language is "+ favorite_languages['sarah'].title()+".")


user_0 = {
    'username':'efemi',
    'first': 'enrico',
    'last':'fermi',
}

for key, value in user_0.items() :
    print("\nKey:" + key)
    print('Value: '+ value)

#looping through all the keys in a dictionary
#page140 / 104

for name in favorite_languages:
    print(name.title())
print("------")
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi "+name.title()+
        ", I see your favorite languae is "+
        favorite_languages[name].title()+"!")
print("-----")

for name in sorted(favorite_languages.keys()):
    print(name.title()+ ", thank you for taking the poll.")

for languae in sorted(favorite_languages.values()):
    print(languae.title())

#A list of dictionaries

alien_1={'color':'green','points':5}
alien_2={'color':'yellow','points':10}
alien_3={'color':'red','points':15}

aliens = [alien_1,alien_2,alien_3]

for alien in aliens:
    print(alien)

#make an empty list for storing aliens
aliens_1=[]

#make 30 green aliens.

for alien_number in range(30):
    new_alien ={'color':'green','points':5,'speed':'slow'}
    aliens_1.append(new_alien)

#show the first 5 aliens:
for alien in aliens_1[:5]:
    print(alien)
print(" . . . .")

#shown how many aliens have been created
print("Total number of aliens: "+str(len(aliens_1)))


####
#A LIST IN A DICTIONARY

#store information about a pizza being ordered

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}

#summarize the order
print("Yuo ordered a "+pizza['crust']+"-crust pizza "+
    "with the following toppings")

for tooping in pizza['toppings']:
    print("\t"+tooping)


favorite_languages2 ={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name, languages in favorite_languages2.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t"+language.title())


#A dictionary in a dictionary 

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princenton',
    },
    'mcuire':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
print("-------------")
for username, user_info in users.items():
    print("\nUsername: "+username)
    full_name = user_info['first']+ " "+user_info['last']
    location = user_info['location']

    print("\tFull name : "+full_name.title())
    print("\tLocations : "+location.title())