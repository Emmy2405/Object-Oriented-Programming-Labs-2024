def odd_index(string):
    result = ""
    for i in range(len(string)):
        if i % 2 != 0:
            result += string[i]

    return result

string = str(input("please enter your string: "))
new_index = odd_index(string)
print("The new string without any odd index characters :", new_index)