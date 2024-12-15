class LinearEquation(object):

    def __init__(self, m, b):
        self.m = m
        self.b = b

    def value(self, x):
        return self.m * x + self.b

    def compose(self, other):

        if not isinstance(other, LinearEquation):
            raise ValueError("Compose is only between linear equations")

        new_m = self.m * other.m
        new_b = self.m * other.b + self.b

        return LinearEquation(new_m, new_b)

    def __add__(self, other):

        if not isinstance(other, LinearEquation):
            raise ValueError("Addition is only between linear equations")

        new_m = self.m + other.m
        new_b = self.b + other.b

        return LinearEquation(new_m, new_b)


    def __str__(self):
        return f"y = {self.m}x + {self.b}"




# Main scope
linear1 = LinearEquation(3.5, 2)  # y = 3.5x + 2
linear2 = LinearEquation(5, 3)  # y = 5x + 3

linear3 = linear1 + linear2

print(linear3)
print(linear3.value(2))