def remove_substring(string, num1, num2):
    return string[:num1] + string[num2:]

result = remove_substring("Hello there", 2, 6)
print(result)