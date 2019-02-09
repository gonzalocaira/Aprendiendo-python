def greet_user(username):
    """Display a simple greeting"""
    print("Hello, "+username.title()+"!")

greet_user('jesse')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')

print("-----")

def get_formatted_name(first_name, last_name, middle_name = ''):
    """ Return a full name, neatly formatted """
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()   

musician = get_formatted_name('jini','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','hendrix')
print(musician)
"""
def get_formatted_name(first_name,last_name):
    full_name = first_name +' '+last_name
    return full_name.title()

musician = get_formatted_name('jini','hendrix')
print(musician)

"""
"""
def  build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)
"""
print("----")
#version 2.0 and 3.0
def build_person(first_name,last_name,age=''):
    #return a dictionary of information abour a person
    person = {'first':first_name,'last':last_name}
    #this part the version 3.0
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',27)
print(musician)


print("---")
def greet_user(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg="Hellouda, "+name.title()+"!"
        print(msg)

usernames = ['hannnah','ty','margot']
greet_user(usernames)

print("---")
def print_models(unprinted_designs,completed_models):
    """
    Simulate priting each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #simulate creating a 3d print from the design
        print("printing model: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    #show all the models that were printed
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

def make_pizza(size,*toopings):
        #print the list of toppings that have been requested.
        print("\Making a "+str(size)+
                "-inch pizza with the following toppings:")
        for tooping in toopings:
                print("- "+tooping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


def build_profile(first,last,**user_info):
        #build a dictionary containing evereything we know about a user
        profile={}
        profile['first_name']=first
        profile['last_name']= last
        for key , value in user_info.items():
                profile[key]= value
        return profile 
user_profile = build_profile('albert','einstein',
                location='princenton',
                field='physics')
print(user_profile)

#Very Important 
#Storing Your Functions In Modules

def make_pizza(size,*toppings):
        print("\nMaking a "+str(size)+
                "-inch pizza with the following toopings:")
        for topping in toppings:
                print("- "+topping)

"""Importing specific functions"""

#--- from module_name import function_name
