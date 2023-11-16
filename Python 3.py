runningTotal = 0

price1 = 12
runningTotal = runningTotal + price1
price2 =24
runningTotal = runningTotal + price2
price3 = 36
runningTotal = runningTotal + price3
price4 = 48
runningTotal = runningTotal + price4

print(runningTotal)

numLines = 0
fin = open("daffodils.txt")
print(fin)
for line in fin:
    print(line)
    numLines = numLines + 1
print(numLines)
        
fin.close()

runTotal1 = 0
numLines1 = 0
answer = 0
fin = open("num_calc_1.txt")
print(fin)
for line in fin:
    line = line.strip()
    if line.isdigit():
        print(line)
        runTotal1 = runTotal1 + int(line)
        numLines1 = numLines1 + 1
    
print(numLines1)
print(runTotal1)

answer = numLines1 / runTotal1
print(answer)

fin.close()

runTotal2 = 0
numLines2 = 0
answer = 0
fin = open("num_calc_2.txt")
print(fin)
for line in fin:
    line = line.strip()
    if line.isdigit():
        print(line)
        runTotal2 = runTotal2 + int(line)
        numLines2 = numLines2 + 1
    
print(numLines2)
print(runTotal2)

answer = numLines2 / runTotal2
print(answer)

fin.close()

a = int(input("Random number"))
b = int(input("Random number"))
c = int(input("Random number"))
d = int(input("Random number"))
e = int(input("Random number"))
f = int(input("Random number"))
g = int(input("Random number"))
h = int(input("Random number"))
i = int(input("Random number"))
j = int(input("Random number"))
k = int(input("Random number"))
l = int(input("Random number"))
m = int(input("Random number"))
n = int(input("Random number"))
o = int(input("Random number"))
p = int(input("Random number"))
q = int(input("Random number"))
r = int(input("Random number"))
s = int(input("Random number"))
t = int(input("Random number"))

NumAns = 0
NumAns = a + b + c + d + e + f + g + h + i + j + k + l + n + m + o + p + q + r + s + t
print(NumAns)
Mean = 20
Ans2 = NumAns / Mean
print(Ans2)


aa = input("Random number1")
bb = input("Random number1")
cc = input("Random number1")
dd = input("Random number1")
ee = input("Random number1")
ff = input("Random number1")
gg = input("Random number1")
hh = input("Random number1")
ii = input("Random number1")
jj = input("Random number1")

fin2 = open("nums3.txt","w")
fin2.write(aa + "\n" + bb + "\n" + cc + "\n" + dd + "\n" + ee + "\n" + ff + "\n" + gg + "\n" + hh + "\n" + ii + "\n" + jj)
fin2.close()