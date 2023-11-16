# Question 16(a)
# Name and School

cardNum=7200828282828210
cardNumstr = str(cardNum)
print(len(cardNumstr))

print(cardNum)

print("Welcome to CardCheck")
CardValidate = int(input("Enter your card number: 7200828282828210"))
x = str(CardValidate)

print("Enter the card expiry date")
ExpiryDate = int(input("11/26 should be entered as 1126:"))
expirydate_str = str(ExpiryDate)

attempts = 0

if len(x) == 16:
    print(type(x[0]))

    cardNumint = int(x[0])
    if cardNumint == 7:
        print("This is a ZincCard")
    elif cardNumint == 8:
        print("This is a WinCard")
        
else:
    attempts = 0
    Validations = 2
    while attempts < Validations:
        print("Please Try Again")
        CardValidate2 = int(input("Enter your card number: 7200828282828210"))
        x= str(CardValidate2)

        if len(cardNumstr) == 16:

            cardNumint = int(x[0])
            if cardNumint == 7:
                print("This is a ZincCard")
            elif cardNumint == 8:
                print("This is a WinCard")
            else:
                print("CardNumber Incorrect")
        attempts = attempts + 1
        
if attempts == 2:
        print("You are blocked")
        exit()
TotalNumber = 0  
for Number in expirydate_str:
    TotalNumber = TotalNumber + int(Number) #reminder, i was adding all expiry numbers, etc, and getting CVV number
    
    
        
#CvvNum = ExpiryDate
#CvvNum = int(input("CVV Number:"))
#cvvTotal      
        






#else x =! cardLength
  #  print("This is incorrect, please try again: CardValidate")