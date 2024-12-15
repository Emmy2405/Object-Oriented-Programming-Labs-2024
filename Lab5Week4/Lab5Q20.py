list1 = [1,2,3,4,5,6]
list2 = [10,9,8,7,6]
output = []

for element in list1:
    if element not in list2:
        output.append(element)


print(output)

#this question is very similar to the removing duplicates just worded a bit differently