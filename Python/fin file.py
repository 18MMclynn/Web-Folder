fin = open("myfile.txt")
print(fin)
for line in fin:
   #^Variable
    print(line)
    
    #print(line.strip())
    
    for line in fin:
    print(line.strip())
    fin.close()
    
    
    fin = open("myfile.txt")          #Read file V
    for line in fin:                  #Check isdigit() V
    line = line.strip()               #Convert to Int() V
    if(line.digit()): #<---int()      #Add to total
    print(line)
    fin.close()