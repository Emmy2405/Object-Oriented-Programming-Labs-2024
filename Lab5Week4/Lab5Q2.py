#where user enters number
num = int(input("Please enter a number:"))

#function to iterate from 0 to that number
def odd_or_even(num):
    #for loop to separate the odd and even numbers
    for i in range(0, num + 1):
        #to print whether the number is odd or even
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")

#calling function
odd_or_even(num)