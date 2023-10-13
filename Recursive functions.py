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
mynum = int(input("Multiply out "))
def times(x):
    if x == 1:
        return 1
    else:
        return x*times(x - 1)
answer = times(mynum)
print(answer)