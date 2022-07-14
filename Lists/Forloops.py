#For loops with the list data type

#This function
for i in range(4):
    print(i)
    
#Is the same as this function
for i in [0,1,2,3]:
    print(i)
    
#If you want to get the list version of the range function  
x = list(range(4))
print(x)

#Pushes out a list that starts at 2, incriments by 5 and stops at 100
x = list(range(2,100,5))
print(x)

#Using an array/list value pointer in a for loop

x = list(range(2,10,2))

for i in range(len(x)):
    print('For index value ' + str(i) + ' :The value in the list is ' + str(x[i]))
    
#Multiple assginment

y=list(range(0,3,1))
print(y)
w, e, r = y

print(w)
print(e)
print(r)