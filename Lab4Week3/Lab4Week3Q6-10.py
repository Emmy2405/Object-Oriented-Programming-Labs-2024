print("\n\nThis is Question 6")
string = str(input("Please enter a sentence: "))
reversed_string = ""

#for loop to put the string in reverse
for character in string:
    reversed_string = character + reversed_string #adding each character to the front

print("The reverse of the string entered: ",reversed_string)

print("\n\nThis is Question 7\n")
import string
sentence = str(input("Please enter your preferred sentence:"))#
lowercase = sentence.lower()
clean_sentence = ""
reversed_sentence = ""
print("The string in all lowercase is:", lowercase)

for char in lowercase:
    if char not in string.punctuation and char not in string.whitespace:
        clean_sentence += char

print("The sentence cleaned without punctuation and whitespaces:", clean_sentence)

#for loop to put the string in reverse
for chars in clean_sentence:
    reversed_sentence = chars + reversed_sentence #adding each character to the front


if clean_sentence == reversed_sentence:
    print("This sentence is a palindrome")
else:
    print("This sentence is not a palindrome")

