#1
'''
alist = [3,2,6,3,7,3,2,7,1,6,7,8,2,6,8,3,2,7,8,2,7,8,3,2,8,7,8,3]
def sumobtainer(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] + sumobtainer(a[1:])
answer = sumobtainer(alist)
print(answer)
'''
#2
'''
mynum = int(input("Multiply out "))
def times(x):
    if x == 1:
        return 1
    else:
        return x*times(x - 1)
answer = times(mynum)
print(answer)

'''
#3
'''
val = input("Enter a number")
val =int(val)
def fibonacci(params):
    if params == 1:
        return 0
    elif params <= 3:
        return 1
    else:
        return(fibonacci(params - 1) + fibonacci(params - 2))
print(fibonacci(val))
'''
#4
'''
inputvalue = int(input("Enter a number"))

def numsum(params):
    if params == 0:
        return 0
    else:
        return params % 10 + numsum(params/10)
    answer = numsum(inputvalue)
    print(answer)'''