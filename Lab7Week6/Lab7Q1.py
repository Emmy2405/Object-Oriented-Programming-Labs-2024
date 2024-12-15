#1. Show the output for the following program. To make it easier, draw a diagram similar to the ones in lecture 9.

str_list = ['hi', 'mom', 'dad', ['grandma', 'grandpa']]
new_list = str_list
copy_list = str_list[:]

str_list[0] = 'bye'
new_list[1] = 'mother'
copy_list[2] = 'father'
copy_list[-1][0] = 'nanna'

print(str_list) # Line 1
print(new_list) # Line 2
print(copy_list) # Line 3

#(a) What output is produced by Line 1 when the program is executed?
# ['bye', 'mother', 'dad', ['nanna', 'grandpa']]

#(b) What output is produced by Line 2 when the program is executed?
#['bye', 'mother', 'dad', ['nanna', 'grandpa']]

#(c) What output is produced by Line 3 when the program is executed?
#['hi', 'mom', 'father', ['nanna', 'grandpa']]
