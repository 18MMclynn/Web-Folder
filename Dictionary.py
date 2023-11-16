sentence = input("Enter a sentence")
chars = {}
vowels = "aeiouAEIOU"
storeVowels = len(vowels)
for char in sentence:
    if char in vowels:
        chars[char] = chars.get(char, 0) + 1
print(chars)

sentence = input("Re-enter sentence")
char = {}
for char in sentence:
     chars[char] = chars.get(char, 0) + 1
print(chars)

'''
sentence = input("Enter a sentence")
chars = {}
for char in sentence:
    print(char)
    if char in chars:
        chars[char] = chars[char] + 1
    else:
        chars[char] = 1
print(chars)
'''



'''
    if char in chars:
        chars[char] = chars[char] + 1
    else:
        chars[char] = 1
        '''


