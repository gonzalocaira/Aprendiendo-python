##
##Working with classes and instances
##

## Point 2: Setting a default value for an attribute
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        #point 2
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    #point 2
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
#point 2
my_new_car.read_odometer()

#modifying an attribute's value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#modifying an attribute's through a method
my_new_car.update_odometer(25)
my_new_car.read_odometer()

#incrementing an attribute's value through a method
my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()