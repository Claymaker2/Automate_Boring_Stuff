# Going to experement more with pythons built in modules.

import random
import math,sys, os

x = random.randint(1,6) # Because of the way we imported the random module, you have to state
# Random.randint in order to use the random int function.

print(x)
print("okay")

from random import * #imports the random module but no longer need to specify the random.randint to
#call the function

x=randint(1,10)
print(x)

#sys.exit() #Exits the program early

#Format of how to use PIP to install new modules. 
#C:\Users\TOsundina\AppData\Local\Programs\Python\Python310\Scripts> pip install camelcase

import pyperclip #Module that allows us to copy and paste text, downloaded using pip

pyperclip.copy("Baller")

print(pyperclip.paste())