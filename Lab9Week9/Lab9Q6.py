class WizCoinPurse:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def value(self):
        # Convert all to knuts
        return (self.galleons * 493) + (self.sickles * 29) + self.knuts

    def weight(self):
        # Calculate weight
        return (
            (self.galleons * 31.103) +
            (self.sickles * 11.34) +
            (self.knuts * 5)
        )


purse = WizCoinPurse(galleons=2, sickles=5, knuts=15)
print(purse)
print(f"Total value in knuts: {purse.value()}")
print(f"Weight of purse: {purse.weight()} grams")
