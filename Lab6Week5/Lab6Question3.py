def prompt_open(mode: str):
    if mode not in ['r','w']:
        raise ValueError("mode must be reading or writing")

    while True:
        filename = input("Enter the file name:")
        try:
            file_handle = open(filename, mode)
            return file_handle
        except FileNotFoundError:
            print("File not found. Please try again") if mode == 'r' else print("Can't open file for writing. Please try again")
        except IOError:
            print("An error occurred. Please try again")


file_handle = prompt_open('r')
print("File opened successfully:", file_handle.name)
file_handle.close()