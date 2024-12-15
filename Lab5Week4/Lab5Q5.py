#where user enters a number
num = int(input("Please enter a number to find its factorial:"))

#function to find the factorial
def factorial(num):
    sum = 1 # variable to hold the factorial value
    #for loop to find the factorial
    for i in range(1,num + 1):
        sum = sum * i

    print("The factorial of", num, "is",sum)

factorial(num)
