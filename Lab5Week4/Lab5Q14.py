def words_beginning_with_o(lists, char):
    sum = 0
    for word in lists:
        if word[0] == char:
            sum += 1

    return sum


lists = []
n = int(input("How many words are you entering:"))

for i in range(n):
    element = input(f"Please enter your {i + 1} word:")
    lists.append(element)
char = input("Please enter your preferred character:")
result = words_beginning_with_o(lists, char)
print(f"The amount of words that begin with {char} in the list is:", result)