#(a) Suppose you want to print a line full of'#' characters. For simplicity, let’s say that a
#line can have only 80 characters. One way is to create a long string to be printed. How would you do it more elegantly #
# in Python using the plus operation (+) of strings?

#(b) Suppose you want to print a column full of '#' characters. For simplicity, let’s
#say that a column could have only 30 characters. Similar to (a), how would you do
#it more elegantly in Python using the multiply operation (*) of strings? Hint: Use
#the newline character (‘\n’).

#part (a)
hash_line = ''

for i in range(80):
    hash_line += '#'

print(hash_line)

#part (b)
column = '#\n' * 30

print(column)
