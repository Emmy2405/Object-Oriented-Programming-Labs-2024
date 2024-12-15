#where user enters number
num = int(input("Please enter a number:"))

#function to print the numbers from 1 to num
def print_number(num):
    #for loop to print the numbers
    for i in range(1,num + 1):
        print(i)

#calling function
print_number(num)