f = open("mean-median-mode-frequency.csv",'r')
line = f.readline()
line = line.strip()
line = line.split(",")
#str(line)
#line.replace("," , " ")
alist = []
print(line)
runningTotal = 0
for item in line:
    alist.append(int(item))
for item in alist:
     runningTotal = runningTotal + (item)
print("Mean is", runningTotal / len(line))
#    line.extend()
print(line)


alist.sort()
mean = len(alist)%2
lenght = len(alist)
print("odd = 1 / even = 0  and this is", mean)
print("this has", lenght , "digits" )
half = len(alist)//2
print("half of", lenght, "is" , half )
median = alist[half]
print("The median is" , median)

print("This is just printing first digit", alist[0])
indexPos = 0
Numlist =[]
Apearlist =[]
while indexPos <= len(alist)-1:
    y = alist.count(alist[indexPos])
    Numlist.append(int(y))
    Apearlist.append(alist[indexPos])
    #print(Apearlist)
    print(y, "thats the amount of" , alist[indexPos] )
    indexPos = indexPos +y
print("Amount of Numbers" , Numlist)
print("The Numbers are" , Apearlist)

Answer = max(Numlist)
print(Answer)
Numlist.index(Answer)
#To find the median
#1  - sort the list alist.sort()
#2 - find the number of items in the list len(alist)
#3 - if the number of items is odd len(alist)%2 == 0 Even, =1 odd
#4 - if odd number, you need to print middle number in the list
#4 - if even number, add the two middle numbers and print the  average
f.close()