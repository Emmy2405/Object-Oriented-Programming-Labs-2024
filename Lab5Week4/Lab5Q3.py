#where user enters number
num = int(input("Please enter a number:"))

#function to iterate from 0 to that number
def multiply(num):
    sum = 0 # variable to store the sum of the number * 9
    #for loop to print the result
    for i in range(0, num + 1):
        #multiplying the number by 9
        sum = i * 9
        #printing it out
        print(i," * 9 = ",sum)

#calling function
multiply(num)
