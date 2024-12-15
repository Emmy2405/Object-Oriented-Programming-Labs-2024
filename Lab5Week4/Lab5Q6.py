string = str(input("Please enter your string:"))

def characters(string):
    length = len(string)

    if length < 4:
        print("String is too short, has to be bigger than 4 characters ")
    else:
        return string[:2] + string[-2:]


print(characters(string))