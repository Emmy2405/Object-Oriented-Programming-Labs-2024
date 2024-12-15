def common_factor(list1, list2):
    for i in list1:
        if i in list2:
            return True

    return False

list1 = [1,2,3,4,5,6]
list2 = [10,9,8,7,6]

result = common_factor(list1, list2)
print(result)