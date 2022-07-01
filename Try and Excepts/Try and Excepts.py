#Debugging your code with try and except statements

def Divider(x):
    try: #Code in this block will execute if there are no errors in the program
        return 42/x
    except ZeroDivisionError: #Will execute if has zero division error
    # Put no error after the except to have the except execute when there is any error.
        print("Error you tried to divide by zero")
        return 0
    
print(Divider(2))
print(Divider(4))
print(Divider(0))
print(Divider(5))