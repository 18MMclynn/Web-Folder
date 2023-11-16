#LinearSearch
'''
inputvalue = int(input("Enter Number"))
alist = [15,4,41,13,24,14,21]

def linears(alist,inputvalue):
    for i in alist:
        if i == inputvalue:
             return alist.index(i)
    return -1

working = linears(alist,inputvalue)
print(working)
'''
#BinarySearch
inputvalue = int(input("Enter Number"))
alist = [0,41,3,7,8,2,10,5,6,9]
alist.sort()
low = 0
high = len(alist)
high = high-1
print(low)
print(high)

while True:
    mid = (low+high)//2
    if alist[mid] == inputvalue:
         print(alist.index(inputvalue))
         break
    elif alist[mid] < inputvalue:
        low = mid + 1
    elif alist[mid] > inputvalue:
        high = mid - 1
    if low > high:
        print("Value not found")
        break
