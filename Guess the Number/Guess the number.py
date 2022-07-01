#Guess the number game. The program will ask you for your name and ask you to
#guess whatever number the program is thinking of. If its wrong it will ask you to guess
#again until you get it right.

import random

print("What is your username? ")
username = str(input())
print("Okay " + username)


x = random.randint(0,10)
counter = 0

#print(str(x))

def main():
    while counter!=5:
        def asker():
            global counter
            print("Im thinking of a number between 0 and 10\nWhat number am I thinking of? ")
            guess = int(input())
            counter = counter + 1
            if guess == x:
                print("Congrats, you guessed the number")
                quit()
            else:
                #print("That was the wrong guess, you have " + counter "guesses left")
                return 0
        asker()
main()

print("The number was " + str(x))
print("You lose!!")
