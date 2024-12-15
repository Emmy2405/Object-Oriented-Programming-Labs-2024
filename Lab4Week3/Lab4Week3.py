print("This is Question 1\n")
#where the user enters the string
string = str(input("Please enter a sentence: "))

for character in string:#for loop to print each character in a single line
    print(character)


print("\n\nThis is Question 2\n")
stringQ2 = "Monty Python"

#part (a)
print("The first character in this string is:", stringQ2[0] )

#part (b)
print("The last character in this string is:", stringQ2[-1] )

#part (c)
print("The last character (including len) in this string is:", stringQ2[len(stringQ2) - 1] )

#part (d)
print("The first word in this string is:", stringQ2[0:4] )


print("\n\nThis is Question 3\n")
S = "Hello"
middle_index = len(S) // 2
#part (a)
print("The middle character in this string is:",S[middle_index])

#part (b)
print("The characters from the beginning up till the middle is:", S[:middle_index] )

#part (c)
print("The characters from the middle up till the end is:", S[middle_index + 1:] )

print("\n\nThis is Question 4\n")
some_string = "Hello world!"
count_O = some_string.count("o")

print("The amount of 'o' in",some_string,"is:",count_O)
#this counts how many o's there are in "hello world"

print("\n\nThis is Question 5\n")
some_string = "Hi!......"
strip = some_string.strip(".!")

print(strip)
#this deletes the characters '.!' from the string and keeps the others
# (basically "strips" those characters from the string)