#Pig Latin is a game of alterations played on words. To make the Pig Latin form of an
#English word the initial consonant sound is transposed to the end of the word and an
#“ay” is affixed. Specifically there are two rules:
#(a) If a word begins with a vowel, append “yay” to the end of the word.
#(b) If a word begins with a consonant, remove all the consonants from the beginning
#up to the first vowel and append them to the end of the word. Finally, append “ay”
#to the end of the word.

#For example:
#dog ⇒ ogday
#scratch ⇒ atchscray
#is ⇒ isyay
#apple ⇒ appleyay

#Write a program that repeatedly prompts for an English word to translate into Pig
#Latin and prints the translated word. If the user enters a period, halt the program.
#Hints:
#Slicing is your friend: it can pick off the first character for checking, and you can slice
#off pieces and concatenate to yield the new word.
#Making a string of vowels allows the use of the in operator: vowels = 'aeiou' .

import string
#delaring variables
vowels = "aeiou"

word = str(input("Please enter a word you would like to translate to Pig Latin:"))

if word[0] == vowels:
    word.append("yay")


