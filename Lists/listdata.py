#The list data type is a value that contains values. 

from re import X


x = ['cat', 'bat', 'lat']
y = [1,2,3,4,5]

print(x) #prints the whole list/array
print(x[0]) #prints first value in the list

#Lists can also contain other lists
z = [x,y]
a = [[4,3,2,5],['pen', 'en']]

print(z) #Will print all lists inside z
print(z[0]) #Will print the first list
print(a[1]) #Will print the second list

x[1] = 8 #Can assign new value to the list. This assigns the second value a value of 8
print(x)
y[1:3] = ['x', 'butt', 'put'] #assign new value starting at second value of list up to the fourth value 
print(y)

del x[1] #Deletes the second value in the list
print(x)

print(len([1,2,3])) #Returns the number of values stored in the list
print(x+y) #Can do list concatination with the plus operator
print(x*3) #can do list multiplication

print(list('hello')) #Turns things into lists

o = 3 in y #Operation that allows you to see if a value is inside a list. 
p = 3 not in y #Operation that allows you to see if a value is not inside a list. 
print(o)
print(p)