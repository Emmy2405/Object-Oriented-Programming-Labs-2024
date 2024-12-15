def insert_string_middle(string, word):
    length = len(string)
    middle_index = length // 2
    return string[:middle_index] + word + string[middle_index:]



result = insert_string_middle("{{}}", "PHP")
print(result)