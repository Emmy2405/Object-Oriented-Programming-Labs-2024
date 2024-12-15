def safe_input(prompt: str, type_input: type):
    while True:
        user_input = input(prompt)
        try:
            return type_input(user_input)
        except ValueError:
            print("Invalid input.")


number = safe_input("Enter a number: ", float)
print("You entered:", number)

