#6. Using list comprehension
#(a) Generate a list of square numbers
list = [1,2,3,4,5,6,7,8,9,10]
square = [n**2 for n in list ]
print(square)

#(b) Convert a list of colors = ['Red', 'Blue', 'Green', 'Black', 'White'] to upper case
colours = ['Red', 'Blue', 'Green', 'Black', 'White']
upper = [n.upper() for n in colours]
print(upper)
#(c) Find all of the numbers from 1-1000 that are divisible by 7
seven = [n for n in range(1,1000) if n %7 == 0]
print(seven)
#(d) Find all of the numbers from 1-1000 that have a 3 in them
three = [ str(n) for n in range(1,1000) if '3' in str(n)]
print(three)
#(d) Count the number of spaces in a string
string1 = 'Hello I am eman'
count = string1.count(' ')
print(count)
#(e) Remove all of the vowels in a string
vowel = 'aeiouAEIOU'
counter = ''.join([n for n in string1 if n not in vowel])
print(counter)
#(f) Find all of the words in a string that are less than 4 letters
words = string1.split()
five = [n for n in words if len(n) < 4]
print(five)
#(g) Challenge! Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9).
# The first part is given below. You need to find out the second list comprehension

var = [number for number in range(1, 1001) if True in [number % n == 0  for n in range(2,10) ]]
print(var)