#8. Write a Python program to combine these two dictionaries adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: d3 = {'a': 400, 'b': 400, 'd': 400, 'c': 300}

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}

for key in d1.keys():
    for k in d2.keys():
        if key == k:
            d3[key] = d1[key] + d2[k]
    if key not in d3:  # Add keys unique to d1
            d3[key] = d1[key]

for k in d2.keys():  # Add keys unique to d2
    if k not in d3:
        d3[k] = d2[k]

print(d3)