def words_beginning_with_o(lists):
    sum = 0
    for word in lists:
        if word[0] == "o":
            sum += 1

    return sum


lists = ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
result = words_beginning_with_o(lists)
print("The amount of words that begin with 'o' in the list is:", result)

