#4. Fractions: You can express a fraction as a tuple: (numerator, denominator).
#(a) Write a function that adds two fractions that are passed as tuples.
#(b) Write a function that multiplies two fractions that are passed as tuples


def addition(fraction1, fraction2):

    numerator = (fraction1[0] * fraction2[1]) + (fraction1[1] * fraction2[0])
    denominator = fraction1[1] * fraction2[1]
    fraction = (numerator, denominator)

    return fraction



def multiplication(fraction1, fraction2):
    numerator =  fraction1[0] * fraction2[0]
    denominator = fraction1[1] * fraction2[1]

    fraction =  (numerator, denominator)

    return fraction




#main scope
fraction1 = (1,2)
fraction2 = (1,2)

result1 = addition(fraction1, fraction2)
result2 = multiplication(fraction1, fraction2)
print(result1)
print(result2)