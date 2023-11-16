'''import random'''
'''
def myfunction():
    num = int(input("Enter a Number "))
    return num
num = myfunction()
print("this is your chosen number - " , num)
def anotherfunction(num):
    x = 1
   # while x != num:
    while not x>num:
        print(x)  
        x += 1  
anotherfunction(num)
'''

#import random
''' 
def rando():
    snum = int(input("Enter small Number "))
    lnum = int(input("Enter large Number "))
    comp_num = random.randint(snum,lnum)
    return comp_num
comp_num = rando()

    
def guessing():
    print("I am thinking of a number")
    mynum = int(input("Enter a Number "))
    return mynum
mynum = guessing()

def check(comp_num, mynum):
    while comp_num != mynum:
        if comp_num > mynum:
            print("you are too low")
            mynum = guessing()
        elif comp_num < mynum:
            print("You are too high")
            mynum= guessing()
    print("correct my number was" , comp_num)

check(comp_num, mynum)
'''
'''
import random
def numbers():
    arany = random.randint(5, 20)
    brany = random.randint(5, 20)
    print(arany , "+" , brany , "= ?")
    x = arany + brany
    ans = int(input("Enter your answere "))
    alist = [x , ans]

    return alist

def numbers2():
    arany = random.randint(25, 50)
    brany = random.randint(1, 25)
    print(arany , "-" , brany , "= ?")
    x = arany - brany
    ans = int(input("Enter your answere "))
    blist = [x , ans]   
    return blist

mynum = 0
while mynum == 00: 
    print("1) Addition ")
    print("2) Subtraction ")
    mynum = int(input("Enter 1 or 2 "))

    if mynum == 1:
        alist = numbers()
        print(alist)
    elif mynum == 2:
        blist = numbers2()
        print(blist)
'''
namelist = ["red"]
    
def addingname():
    addname = input("Add a name")
    return addname

def deletename():
    removename = imput("remove a name")
    return removename

def changename():
    migratename = input("vchange a namw")
    return migratename

#print(namelist)
   
   
   
   
   
'''
inputt = 0
while inputt == 00: 
    print("1) Add Name ")
    print("2) Remove Name ")
    print("3) Change Name ")
    print("?) any other number to end program")
    mynum = int(input("Choose your Program"))

    if mynum == 1:
        alist = addingnames()
        namelist.append(alist)
        print("You choose to add a name" , alist)
        print("Your list now like")
        print("\n", namelist)
        print("\n \n")
        mynum = 0
        
    elif mynum == 2:
        alist = deletename()
        namelist.remove(alist)
        print("You choose to remove a name" , alist)
        print("Your list now like")
        print("\n", namelist)
        print("\n \n")
        mynum = 0
        
    elif mynum == 3:
        alist = changename()
        namelist.(alist)
        replacename = input("Replace the name with")
        print("You choose to change a name" , alist, "into" , replacename)
        print("Your list now like")
        print("\n", namelist)
        print("\n \n")
        mynum = 0 
    
print(namelist)
'''


namelist = ["red","blu"]
def addingname(addname):
    namelist.append(addname)
def deletename(removename):
    namelist.remove(removename)
def changename(migratename,replacename,namelist):
    z = namelist.index(migratename) 
    namelist[z] = replacename
    
inputt = 0
while inputt == 0: 
    print("1) Add name ")
    print("2) Remove name ")
    print("3) change name ")
    print("?) any other number to end program ")
    mynum = int(input("Choose your program \n  " ))    
    if mynum == 1:
        print(namelist)
        addname = input("Add a name ")
        addingname(addname)
        print(namelist)      
    elif mynum == 2:
        print(namelist)
        removename = input("remove a name ")
        deletename(removename)
        print(namelist)     
    elif mynum == 3:
        print(namelist)
        migratename = input("change a name ")
        replacename = input("Replace the name with ")
        changename(migratename,replacename,namelist)
        print("you chose to change the name" , migratename , "into" , replacename )
        print("your list now looks like")
        print("\n", namelist)   
        mynum = 0
    else:
        break
    
z = namelist.index(migratename) 
    namelist[z] = replacename
def addfile():
    f=open("Salaries.csv",'a')
    f.write(input("Add your name "))
    f.write(" , ")
    f.write(input("Add salary amount "))
    print("\n")
    f.write("\n")
    f.close()
def viewrecords():
    f=open("Salaries.csv",'r')
    z = f.read()
    print(z)
    f.close()
    
inputt = 0
while inputt == 0:
    print("1) Add to file ")
    print("2) View All records ")
    print("3) Quit Program ", "\n")
    mynum = int(input("Put in a number "))
    if mynum == 1:
        addfile()
    elif mynum == 2:
        viewrecords()
    elif mynum == 3:
        break
    else:
        print("please select value 3 to exit program")