#This module teaches us how to write our own functions in python

from re import X


def hello():
    print("Fuck off")
    print('You')
    print(325)
    return 0

hello()
hello()

#Pass in arguments into the functions. Before the argument is passed it 
#is know as a parameter. 


def combo(name): #name is the parameter in this example
    print('Hello ' + name )
    return 0

combo('Alice') #Alice is the argument in this example
print("What name do you want to input? ")
x=name=str(input())
combo(x)

#Using the return function

def addition(numba):
    return numba+2

t = addition(3)
print(str(t))