# Example showing how to do For loops in python sd

def One(): #For statement that starts at 0, ends at 9 and increases by 1 each time
    for x in range(10):
        print(str(x))
        y = len(str(x)) #len gives you the length of the argument, for strings would tell you how many characters in it. 
        print(y)
    return x

def Twelve(): #For Statement that starts at 12, ends at 15 and increases by 1 each time
    for x in range(12,16):
        print(str(x))
        y = len(str(x))
        print(y)
    return x

def Two(): #For Statement that starts at 0, ends at 14 and increments by two each time
    for x in range (0,16,2):
        print(str(x))
        y = len(str(x))
        print(y)
    return x

def Main():
    print("Which function would you like to run? ")
    Func = input()
    if(Func == "Twelve"):
        Twelve()
    elif(Func == "One"):
        One()
    elif(Func == "Two"):
        Two()
    else:
        print("Thats not a valid entry ")
        Main()

Main()