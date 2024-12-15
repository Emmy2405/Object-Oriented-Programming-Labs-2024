#7. If my_dict = {'a':15 , 'c':35, 'b':20}, write Python code:
my_dict = {'a':15 , 'c':35, 'b':20}
#(a) to print all the keys.
for key in my_dict:
    print(key)
#(b) to print all the values.
for values in my_dict.values():
    print(values)
#(c) to print all the keys and values pairs.
for key, values in my_dict.items():
    print(key, values)
#(d) to print all the keys and value pairs in order of key.
for key in sorted(my_dict.keys()):
    print(key)
#(e) to print all the keys and value pairs in order of value.
for values in sorted(my_dict.values()):
    print(values)