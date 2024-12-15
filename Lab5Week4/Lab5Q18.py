def duplicates(list1):
    new_list = []
    for i in list1:
        if i not in new_list:
            new_list.append(i)

    return new_list

list1 = [1,1,2,2,3,3,4,4,5,5,6,6]
result = duplicates(list1)
print(result)