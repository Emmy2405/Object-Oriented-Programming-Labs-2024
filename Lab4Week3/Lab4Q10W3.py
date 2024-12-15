#Although Python’s formatted printing can be cumbersome, it can often drastically
#improve the readability of output. Try creating a table out of the following values:

#Melting and Boiling Points of Alkanes
#Name		Melting Point (deg C)		Boiling Point (deg C)
#Methane          -162				            -183
#Ethane		       -89				            -172
#Propane	       -42				            -188
#Butane		       -0.5				            -135

#array to store the values of the table
alkanes = [
    ("Methane", -162, -183),
    ("Ethane", -89, -172),
    ("Propane", -42, -188),
    ("Butane", -0.5, -135)
]
#here we print the title and thw table header
print("Melting and Boiling Points of Alkanes")
print(f"{"Name" :<10} {"Melting Point (deg C)" :<25} {"Boiling Point (deg C)" :<25}")

#here we are printing the table values into their position
for name, melting_point, boiling_point in alkanes:
    print(f"{name:<10} {melting_point :<25} {boiling_point :<25}")