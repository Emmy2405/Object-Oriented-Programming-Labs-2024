#Question 5
a = 3
b = 4
c = 5

d = (a + b) * c

print(d)

#Question 7
int_a = 27
int_b = 5
int_a2 = 6
print(int_a) # Line 1
print(int_b + 5) # Line 2
print(int_b) # Line 3

#Question 8
a_float = 2.5
a_int = 7
b_int = 6
print(a_int / b_int) # Line 1
print(a_int // a_float) # Line 2
print(a_int % b_int) # Line 3
print(int(a_float)) # Line 4
print(float(a_int)) # Line 5

#Question 9
a_int = 10
b_int = 3
c_int = 2
print(a_int + b_int * c_int) # Line 1
print( (a_int + b_int) * c_int ) # Line 2
print(b_int ** c_int) # Line 3

#Question 10
length = 12
width = 2
area = length * width
print("The area of a rectangle with length", length, "and width", width,"is", area)

#Question 11
a = int(input("Please enter your number"))

answer = ((((a + 2) * 3 ) - 6) / 3)

print(answer)

#Question 13
my_var1 = 7.0
my_var2 = 5
print(my_var1 % my_var2)

#Question 14
a = input("Please enter anything:")

print(str(a))
print(int(a))
print(float(a))

#Question 15
#A = 'a'
#B = 'b'
#C = 'c'

#D = (a + b) * c

#print(D)

#Question 16

e = int(input("Please enter a number:"))

if e % 2 == 0:
    e = True
    print(0)
else:
    e = False
    print(1)

#Question 17
weight = float(input("Please enter your weight in kg:"))
height = float(input("Please enter your height in metres:"))

BMI = weight / (height ** 2.0)

print("Your BMI is", BMI)

weight1 = float(input("Please enter your weight in pounds:"))
height1 = float(input("Please enter your height in inches:"))

kg = weight1 * 0.453592
metres = height * 0.0254

BMI2 = kg / (metres ** 2.0)

print("Your BMI converted  is", BMI2)