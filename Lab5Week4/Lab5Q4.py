#where user enters a number
num = int(input("please enter a number:"))

#function to print out the sum
def addition(num):
    #declaring the variable
    sum = 0
    #for loop to add the numbers together
    for i in range(1,num + 1):
        sum = sum + i
    #printing out the sum
    print("The sum of all the numbers is:",sum)

#calling function
addition(num)
