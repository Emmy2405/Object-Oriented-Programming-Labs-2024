def even_length(string):
    length = len(string)
    new_string = ""
    if length % 2 != 0:
        print("String doesn't have even number of characters")
        return
    else:
        if length % 2 == 0:
            result = string[:length // 2]
            return result


result = even_length("Python")
print(result)
