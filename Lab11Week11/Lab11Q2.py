class WholeNumber(object):

    def __init__(self, value=0):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Whole number must be a non negative integer")

        self.value = value

    def __add__(self, other):

        if not isinstance(other, WholeNumber):
            raise ValueError("Whole numbers can only be added with Whole numbers")

        return WholeNumber(self.value + other.value)


    def __sub__(self, other):

        if not isinstance(other, WholeNumber):
            raise ValueError("Whole numbers can only be subtracted with Whole numbers")

        return WholeNumber(self.value - other.value)


    def __mul__(self, other):
        if not isinstance(other, WholeNumber):
            raise ValueError("Whole numbers can only be subtracted with Whole numbers")

        return WholeNumber(self.value * other.value)

    def __str__(self):
        return f"{self.value}"


# Main scope
n1 = WholeNumber(5)
n2 = WholeNumber(3)

n3 = n1 + n2
print("Addition")
print(n3)

n3 = n2 - n1
print("subtraction")
print(n3)

n3 = n1 * n2
print("multiplication")
print(n3)