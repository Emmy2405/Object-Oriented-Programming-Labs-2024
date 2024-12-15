

#-----------------------------------------------------------------------------------------------------------------------------------
class Currency:
    """A class to represent an amount in a specific currency and allow operations like conversion, addition, and comparison."""

    RATES = {("EUR", "USD"): 1.069229,
             ("USD", "EUR"): 0.939218,
             ("EUR", "GBP"): 0.860186,
             ("GBP", "EUR"): 1.15896,
             ("USD", "GBP"): 0.81039,
             ("GBP", "USD"): 1.23396}

    VALID_CURRENCIES = ['USD', 'EUR', 'GBP']

    def __init__(self, amount=1, currency_type='EUR'):
        """
        Initialize a Currency object.
        :param amount: The numeric amount of the currency.
        :param currency_type: The three-letter code representing the currency type.
        """
        if currency_type in Currency.VALID_CURRENCIES:
            self.amount = amount
            self.currency_type = currency_type
        else:
            print("Invalid currency type: {}\n".format(currency_type))
            self.amount = 0
            self.currency_type = ''

    def convert_to(self, new_currency_type: str):
        """
        Convert the currency to another type.
        :param new_currency_type: The target currency type.
        :return: A new Currency object with the converted amount and currency type.
        """
        if new_currency_type == self.currency_type:
            return Currency(self.amount, self.currency_type)

        if new_currency_type not in Currency.VALID_CURRENCIES \
                or self.currency_type not in Currency.VALID_CURRENCIES:
            print("Conversion from {} to {} not allowed".format(self.currency_type, new_currency_type))
            return None

        rate = Currency.RATES.get((self.currency_type, new_currency_type))
        if not rate:
            print("No conversion rate available for {} to {}".format(self.currency_type, new_currency_type))
            return None

        amount = self.amount * rate
        print("{:.2f} {} => {:.2f} {}".format(self.amount, self.currency_type, amount, new_currency_type))
        return Currency(amount, new_currency_type)

    def __str__(self):
        """Return the amount and type as a string."""
        return "{:.2f} {}".format(self.amount, self.currency_type)

    def __repr__(self):
        """Return a string representation suitable for debugging."""
        return "Currency(amount={}, currency_type='{}')".format(self.amount, self.currency_type)

    def __add__(self, other):
        """Add two Currency objects or a Currency and a numeric value."""
        if isinstance(other, Currency):
            other_converted = other.convert_to(self.currency_type)
            return Currency(self.amount + other_converted.amount, self.currency_type)
        elif isinstance(other, (int, float)):
            return Currency(self.amount + other, self.currency_type)
        else:
            raise TypeError("Unsupported operand type for +: 'Currency' and '{}'".format(type(other).__name__))

    def __radd__(self, other):
        """Reverse addition to handle numeric + Currency."""
        return self.__add__(other)

    def __sub__(self, other):
        """Subtract two Currency objects or a Currency and a numeric value."""
        if isinstance(other, Currency):
            other_converted = other.convert_to(self.currency_type)
            return Currency(self.amount - other_converted.amount, self.currency_type)
        elif isinstance(other, (int, float)):
            return Currency(self.amount - other, self.currency_type)
        else:
            raise TypeError("Unsupported operand type for -: 'Currency' and '{}'".format(type(other).__name__))

    def __rsub__(self, other):
        """Reverse subtraction to handle numeric - Currency."""
        if isinstance(other, (int, float)):
            return Currency(other - self.amount, self.currency_type)
        else:
            raise TypeError("Unsupported operand type for -: '{}' and 'Currency'".format(type(other).__name__))

    def __gt__(self, other):
        """Compare two Currency objects based on their amount after conversion."""
        if isinstance(other, Currency):
            other_converted = other.convert_to(self.currency_type)
            return self.amount > other_converted.amount
        else:
            raise TypeError("Unsupported operand type for >: 'Currency' and '{}'".format(type(other).__name__))


# Main Program
if __name__ == "__main__":
    curr = Currency(7.50, 'USD')
    curr2 = Currency(2, 'EUR')
    print(curr)  # 7.50 USD
    print(curr2)  # 2.00 EUR

    # Test conversion
    new_curr = curr2.convert_to("USD")  # 2.00 EUR => 2.14 USD
    print(new_curr)  # 2.14 USD

    # Test addition
    sum_curr = curr + curr2  # 7.50 USD + 2.00 EUR
    print(sum_curr)  # 9.64 USD

    # Test numeric addition
    sum_curr2 = curr + 5.5
    print(sum_curr2)  # 13.00 USD

    # Test subtraction
    sub_curr = curr - curr2  # 7.50 USD - 2.00 EUR
    print(sub_curr)  # 5.36 USD

    # Test numeric subtraction
    sub_curr2 = 20 - curr
    print(sub_curr2)  # 12.50 USD

    # Test comparison
    print(curr > curr2)  # True if 7.50 USD > 2.00 EUR
