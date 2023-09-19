
#020, 021, 022
username = input("enter name in lowercase ")
second_username = input("enter 2nd name in lowercase ")
username_title = username[0].upper() + username[1:]
second_username_title = second_username[0].upper() + second_username[1:]
store = len(username)
full_username = username_title + " " + second_username_title
print(full_username)
#print(username_title)
#print(second_username_title)
#print(type(username))
#print(type(second_username))
#whole_username = username + " " + second_username
#print(whole_username)
#len(username)
#print(username[:])

#024
word_of_choice = input("enter any word in lowercase ")
capitalise_word = word_of_choice.upper()
print(capitalise_word)

#025
username2 = input("enter name in lowercase ")
length_of_name = len(username)
if(length_of_name < 5):
           second_username2 = input("enter 2nd name in lowercase ")
           username_title2 = username2[0].upper() + username2[1:]
           second_username_title2 = second_username2[0].upper() + second_username2[1:]
           full_username2 = username_title2 + " " + second_username_title2
           print(full_username2)
elif(length_of_name > 5):
           username_title2 = username2[0].upper()
           print(username2)
