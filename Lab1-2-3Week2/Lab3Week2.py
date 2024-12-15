#Question 1 - Grades

print("\nThis is Question 1")
mark = int(input("Please enter a mark:"))

if mark > 40:
    print("This is a pass")
elif mark <= 40:
    print("This is a fail")


#Question 2 - greater, less than or equal to
print("\nThis is Question 2")

num1 = int(input("Please enter a number:"))
num2 = int(input("Please enter a second number:"))

if num1 > num2:
    print("Num1 is greater than Num2")
elif num1 < num2:
    print("Num1 is less than Num2")
else:
    print("Both numbers are equal")


#Question 3 - calculator
print("\nThis is Question 3")
var1 = int(input("\nPlease enter a number:"))
var2 = int(input("\nPlease enter a second number:"))
operation = input("Please enter an operation(+, -, *, /):")
sum = 0

if operation == '+' :
    sum = var1 + var2
elif operation == '-':
    sum = var1 - var2
elif operation == '*':
    sum = var1 * var2
elif operation == '/':
    sum = var1 / var2
else:
    print("Operation not found")

print("The sum of both numbers is :", sum)

#Question 4 - largest number
print("\nThis is Question 4")
var3 = int(input("\nPlease enter a number:"))
var4 = int(input("\nPlease enter a second number:"))
var5 = int(input("\nPlease enter a third number:"))

largest = max(var3, var4, var5)

print("The largest number is ", largest)

#Question 5 - output of following program

print("\n This is Question 5")
user_str = input("Enter a positive integer:") # Line 1
my_int = int(user_str)
count = 0
while my_int > 0:
   if my_int % 2 == 1:
       my_int = my_int//2
   else:
       my_int = my_int - 1
   count += 1 # Line 2
print(count) # Line 3
print(my_int) # Line 4

#(a) 4
#(b) 0
#(c) str
#(d) increment operator
#(e) beginning of block of code that belongs to that statement


#Question 6 - Cigars
print("\nThis is question 6")
#(a)
cigars = int(input("Please enter number of cigars consumed:"))
weekend = input("Please enter if it's during the weekend(y/n):")

#(b)
temp = float(input("Please enter the temperature:"))
season = input("Is it summer? (y/n)")

#(c)
speed = input("Please enter the speed:")
birthday = input("Is it your birthday:(y/n)")

#Question 7 - divisible by 17
print("\nThis is Question 7")
num = 100
count = 0

while num <= 999 :
    if num % 17 == 0:
        count += 1
        print(num)
    num += 1

print("The amount of numbers divisible by 17 is : ", count)

#Question 8
print("\nThis is Question 8")

#(a)
X = int(input("Please enter an integer:"))
sum1 = 0

for consecutive_integer in range (1, X + 1):
    sum += consecutive_integer

print(sum)

#(b)
X2 = int(input("Please enter an integer:"))
sum2 = 0

for n in range (1, X + 1):
    sum2 = 0
    for consecutive_integer2 in range (1, n + 1):
        sum2 += consecutive_integer2

    print(sum2)

#(c)
print("This is Q8. part c")
X2 = int(input("Please enter an integer:"))
sum2 = 0

for n in range (1, X + 1):
    sum2 = 0
    for consecutive_integer2 in range (1, n + 1):
        sum2 += consecutive_integer2

    if sum2 % n ==0:
        print(sum2)


