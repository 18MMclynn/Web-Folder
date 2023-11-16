'''
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C

DWKOQH FRJJXQLWB FROODJH

26

what do you when you
cross a snowman with a
vampire ? frostbite
'''

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc"
key = 3
txt = input("Random txt ")
#string.replace(alphabet,cipher)
for variable1 in txt:
    if variable1 in alphabet:
        position_of_current_letter =alphabet.index(variable1)
        position_of_encoded_letter = position_of_current_letter + key
        print(alphabet[position_of_encoded_letter])
        




number = "12345678901"
key1 = 3
txt = input("Random txt ")
#string.replace(alphabet,cipher)
for variable2 in txt:
    if variable2 in number:
        position_of_current_letter =number.index(variable2)
        position_of_encoded_letter = position_of_current_letter + key1
        print(number[position_of_encoded_letter])













'''
def encrypt_func(txt, s)
result = ""
for i in range(len(txt)):
    char = txt[i]
    if (char.isupper()):
        result += chr((ord(char) + s - 64) % 26 +65)
        else:
            result += chr((ord(char) + S -96) % 26 +97)
            return result
        
        txt = input("Random txt"
            
        '''