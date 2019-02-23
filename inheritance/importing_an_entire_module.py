#You can also import an entire module and then access the classes you need
#using dot notation. 
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

""" Importing all classes from a module"""

#from module_name import *

#be careful

#This method is not recommended for two reasons. First, it’s helpful
#to be able to read the import statements at the top of a file and get a clear
#sense of which classes a program uses.