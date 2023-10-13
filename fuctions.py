import random
'''
def myfunction():
    num = int(input("enternumber "))
    return num     
num = myfunction()
print("this is ur chosen number = ", num)
def anotherfunction(num):
    x = 1
   # while x != num+1:
    while not x>num:
        print(x)
        x += 1 
anotherfunction(num)
'''



'''
def rando():
    snum = int(input("enternumber small "))
    lnum = int(input("enternumber large "))
    comp_num = random.randint(snum, lnum)
    return comp_num

comp_num = rando()

def guessing():
    print("I am thinking of a number...")
    mynum = int(input("enternumber guess "))
    return mynum
mynum = guessing()


def check(comp_num, mynum):
    while comp_num != mynum:
        if comp_num > mynum:
            print("you are too low")
            mynum = guessing()   
        elif comp_num < mynum:
            print("you are too High")
            mynum = guessing()   
    print("correct my number was", comp_num)
    
check(comp_num, mynum)
'''

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
    alist = [x , ans]   
    return alist

def compare(alist):
    if alist[0] - alist[1] ==0:
        print("Correct")
    else:
        print("incorrect")
        print(" The correct answer was" , alist[0])
  


mynum = 0
while mynum == 00: 
    print("1) Addition ")
    print("2) Subtraction ")
    mynum = int(input("Enter 1 or 2 "))

    if mynum == 1:
        alist = numbers()
        print(alist)
    elif mynum == 2:
        alist = numbers2()
        print(alist)
    compare(alist)
'''      
 # incomplete
 

namelist = ["red","blu"]
   
def addingname(addname):
    namelist.append(addname) 

def deletename(removename):
    namelist.remove(removename)
    
def changename(migratename,replacename,namelist):
    z = namelist.index(migratename) 
    namelist[z] = replacename

input2 = 0
while input2 == 0: 
    print("1) Add name ")
    print("2) Remove name ")
    print("3) change name ")
    print("?) any other number to end program ")
    mynum = int(input("Choose your program \n  "))    
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
        replacename = input("Replace the name with ")#the name thats will replace current name
        changename(migratename,replacename,namelist) #calls function & gets name thats gonna be changed 
 
        print("you chose to change the name" , migratename , "into" , replacename )

        print("your list now looks like")
        print("\n", namelist)   
        mynum = 0
        
    else:
        break


#f = open("Salaries.csv",'w+')
#f.close

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


input2 = 0
while input2 == 0:
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



def addfile():
    f=open("Salaries.csv",'a')
    f.write(input("Add your name "))
    f.write(",")
    f.write(input("Add salary amount "))
    print("\n")
    f.write("\n")
    f.close()
    
def viewrecords():
    f=open("Salaries.csv",'r')
    z = f.read()
    print(z)
    f.close()

def deleterecord():
    f=open("Salaries.csv",'r')
    #alist = f.readline()
    alist=[]
    for line in f:
        line = line.strip()
        alist.append(line)
    #alist = ["red,100","blu,150"]
    print("Start with 0,1,2,3,4....")
    input3 = int(input("enter the number of the record you want to delete "))
    positon = alist.pop(input3)
    
    print("you chose to delete the record ", positon)
 
    
    #print(alist)
    f.close()
    f=open("Salaries.csv",'w')
    for separate in alist:
         f.write(separate)
         f.write("\n")
        
        
    #s = str(alist)
    #f.write(s)
    
    f.close()


input2 = 0
while input2 == 0:
    print("1) Add to file ")
    print("2) View All records ")
    print("3) Delete a record ")
    print("4) quit program", "\n")
    mynum = int(input("Put in a number "))
    if mynum == 1:
        addfile()
    elif mynum == 2:
        viewrecords()
    elif mynum == 3:
        deleterecord()
    elif mynum == 4:
        
        break
    else:
        print("please select value 4 to exit program")
        
        

        
        
        
        #z = namelist.index(migratename) 
    #namelist[z] = replacename

        

        