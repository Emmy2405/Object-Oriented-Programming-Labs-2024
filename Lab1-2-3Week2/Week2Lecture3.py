
#code for perfect number
number = int(input("Please enter a number:"))
sum = 0

for d in range(1, int(number/2)):
    if number % d == 0:
        sum += d

if sum == number:
    print(number, "is perfect")
else:
    print(number, "is not perfect")


