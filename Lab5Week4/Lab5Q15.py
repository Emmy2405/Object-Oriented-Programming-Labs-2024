def even_list(lists):
    count = 0
    new_list = []
    for i in lists:
        if i % 2 == 0:
            new_list.append(i)

    return new_list

lists = [1, 2, 3, 4, 5, 6]
result = even_list(lists)
print("The new list with all even numbers is:",result)