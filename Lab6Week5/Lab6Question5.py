file_str = input("Open what file:")
find_line_str = input("Which line (integer):")

try:
   input_file = open(file_str)  # potential user error
   find_line_int = int(find_line_str)  # potential user error
   line_count_int = 1
   for line_str in input_file:
       if line_count_int == find_line_int:
           print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
           break
       line_count_int += 1
   else:
       # get here if line sought doesn't exist
       print("Line {} of file {} not found".format(find_line_int, file_str))
       input_file.close()
except IOError:
   print("The file", file_str, "doesn't exist.")
except ValueError:
   print("Line", find_line_str, "isn't a legal line number.")

print("End of the program")

#(a) When IOError occurred the user had to enter a line number before the error occurred. Rewrite the code so that if a bad file name is entered, the error will be handled before a line number is requested.
file_str = input("Open what file:")
try:
   input_file = open(file_str)  # potential user error
except IOError:
   print("The file", file_str, "doesn't exist.")
else:
   find_line_str = input("Which line (integer):")
   try:
      find_line_int = int(find_line_str)  # potential user error
      line_count_int = 1
      for line_str in input_file:
         if line_count_int == find_line_int:
            print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
            break
         line_count_int += 1
      else:
         # get here if line sought doesn't exist
         print("Line {} of file {} not found".format(find_line_int, file_str))
      input_file.close()
   except ValueError:
      print("Line", find_line_str, "isn't a legal line number.")

print("End of the program")

#(b) Rewrite the code so that if IOError occurs the program keeps asking for input until the user gets it right
while True:
   file_str = input("Open what file:")
   try:
      input_file = open(file_str)  # potential user error
   except IOError:
      print("The file", file_str, "doesn't exist.")
   else:
      break

while True:
   find_line_str = input("Which line (integer):")
   try:
      find_line_int = int(find_line_str)  # potential user error
      break
   except ValueError:
      print("Line", find_line_str, "isn't a legal line number.")

line_count_int = 1
for line_str in input_file:
   if line_count_int == find_line_int:
      print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
      break
   line_count_int += 1
else:
   # get here if line sought doesn't exist
   print("Line {} of file {} not found".format(find_line_int, file_str))
input_file.close()

print("End of the program")

#(c) Rewrite the code so that if error ValueError occurs the program keeps asking for input until the user gets it right.

file_str = input("Open what file:")
while True:
   try:
      input_file = open(file_str)  # potential user error
      break
   except IOError:
      print("The file", file_str, "doesn't exist.")
      file_str = input("Open what file:")

while True:
   find_line_str = input("Which line (integer):")
   try:
      find_line_int = int(find_line_str)  # potential user error
      break
   except ValueError:
      print("Line", find_line_str, "isn't a legal line number.")

line_count_int = 1
for line_str in input_file:
   if line_count_int == find_line_int:
      print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
      break
   line_count_int += 1
else:
   # get here if line sought doesn't exist
   print("Line {} of file {} not found".format(find_line_int, file_str))
input_file.close()

print("End of the program")
