#Write a Python program that will “encrypt” a string. The encryption algorithm we’ll use is to add 1 to the ASCII code,
# so ‘a’ becomes ‘b’, ‘b’ becomes ‘c’, etc.
# The string ‘abc’ becomes ‘bcd’. You’ll need to use the functions ord() and chr() discussed in class

#Hint: To encrypt the letter ‘a’ take the ASCII code of ‘a’ 97, add 1 (98) and find the

string = str(input("Please enter a string: "))
encrypted = ""


for char in string:
    encrypted += chr(ord(char) + 1)

print(encrypted)

#for i, char in enumerate(string):
    #encrypted += chr(ord(char) + i)

#print(encrypted)