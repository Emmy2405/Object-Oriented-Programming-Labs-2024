def get_tuple(movie_year: str) -> tuple:
    """Given a movie year as 'Movie name (year)', return a tuple ('Movie name', 'year')"""
    movie, year = movie_year.split("(")
    movie = movie.strip()
    year = year.strip(")\n")
    return movie, year

def create_dictionary() -> dict:
    """Create a dictionary from a file with movie-actor data."""
    file_name = input("Open what file: ")
    while True:
        try:
            file = open(file_name, "r")
            break
        except FileNotFoundError:
            print("File not found")
            file_name = input("Open what file (or 'exit' to leave): ")
            if file_name.lower() == 'exit':
                exit()

    data = {}  # {("Meet Joe Black", 1998): {"Brad Pitt"}}
    for line in file:
        line = line.strip()
        line_list = line.split(",")
        actor = line_list[0]
        for movie_year in line_list[1:]:
            movie, year = get_tuple(movie_year)

            if (movie, year) in data:
                data[(movie, year)].add(actor)
            else:
                data[(movie, year)] = {actor}

    file.close()
    return data

def menu() -> None:
    """Display a menu for the user to perform set operations on movies."""
    while True:
        user_input = input("Enter 2 movies as 'name (year)' separated by an operator (&, |, -) or enter '.' to quit: ")
        if user_input == ".":
            break

        if any(op in user_input for op in "&|-"):
            operator = "&" if "&" in user_input else "|" if "|" in user_input else "-"
            movie1, year1 = get_tuple(user_input.split(operator)[0].strip())
            movie2, year2 = get_tuple(user_input.split(operator)[1].strip())

            if (movie1, year1) not in data_dictionary:
                print(f"{movie1} ({year1}) not in the database")
                continue
            if (movie2, year2) not in data_dictionary:
                print(f"{movie2} ({year2}) not in the database")
                continue

            if operator == "&":
                result = data_dictionary[(movie1, year1)] & data_dictionary[(movie2, year2)]
            elif operator == "|":
                result = data_dictionary[(movie1, year1)] | data_dictionary[(movie2, year2)]
            elif operator == "-":
                result = data_dictionary[(movie1, year1)] - data_dictionary[(movie2, year2)]

            print(f"Result: {result}")
        else:
            print("Operation not recognized. Use &, |, - to separate movies.")

# Main scope
data_dictionary = create_dictionary()
print(data_dictionary)
menu()
