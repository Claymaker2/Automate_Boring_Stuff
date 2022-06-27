# This Code will serve as a basic reminder of how to use If, Else, and elsif statements
# Def commands are also used

def choosebuilding():
    building = 0
    while(building != '1' and building != '2'):
        print("What building would you like to run into? ")
        building = input()
        if(building=='1' or building =='2'):
            print("You have chosen building " + str(building))
    
    return choosebuilding
3
    
choosebuilding()