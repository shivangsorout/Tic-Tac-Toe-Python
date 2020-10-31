'''
# for importing a package

import examplemod

examplemod.i_can_do_something()
'''

'''
# for minimizing examplemod.function

from examplemod import i_can_do_something

i_can_do_something()
'''

'''
# we do this for 2 or more functions
from examplemod import i_can_do_something, i_can_do_anything

i_can_do_anything()
i_can_do_something()
'''

'''
# for shortening the name of function

from examplemod import i_can_do_something as icds

icds()
'''

'''
# this for the package which is in the folder of name mod

from mod.exampledir import i_can_do_something,i_can_do_anything

i_can_do_anything()
i_can_do_something()
'''

'''
# this is used when there are lots of functions but this is not recommended because 
# when someone have to edit the function he/she won't be able to know that where the function is.

from examplemod import *

i_can_do_something()
i_can_do_anything()
'''

#for cmd for installing the package
#pip install numpy
#pypi.org (python package index)
#or
#py -3.9 -m pip install colorama


'''
# This is the concept of dictionary

dictionary = {'noob':8,'poop':69}
print(dictionary['noob'])
dictionary['cat'] = 3
for i in dictionary:
	print(i)

for i in dictionary:
	print(dictionary[i])
'''

'''
# For colouring the stuff
from colorama import Fore, Back , Style , init
init()
print(Fore.GREEN + '0' + Style.RESET_ALL)
'''