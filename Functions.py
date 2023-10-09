import random
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
