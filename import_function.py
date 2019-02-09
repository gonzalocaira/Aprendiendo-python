"""
# first try
import functions

functions.make_pizza(16,'pepperoni')
functions.make_pizza(12,'mushrooms','green peppers',
                'extra cheese')
"""
from functions import make_pizza

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers',
                'extra cheese')


#Using as to Give a Function an Alias

#from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

"""from module_name import function_name as alias_name"""

#Using as to Give a module an Alias

#import pizza as P
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#importing all functions in a module

#from pizza import *