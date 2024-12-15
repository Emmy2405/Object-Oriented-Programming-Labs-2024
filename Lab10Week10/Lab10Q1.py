#There are websites such as https://www.carsireland.ie/ that provide
# information about secondhand vehicles. Design a base class for vehicles
# with fields such as model year, total mileage, Vehicle Identification
# Number (VIN), engine, transmission, options, and etc. Design subclasses
# for car, truck, SUV, and minivan. Think about the specific fields and
# methods required for the subclasses. Instantiate your classes with
# examples so you can test your code.


class Vehicle:
    def __init__(self, model_year, mileage, vin, engine, transmission, options):
        """
        Initialize a generic Vehicle with common attributes.
        """
        self.model_year = model_year
        self.mileage = mileage
        self.vin = vin
        self.engine = engine
        self.transmission = transmission
        self.options = options

    def __str__(self):
        """
        String representation of a Vehicle object.
        """
        details = f"Model Year: {self.model_year}\nMileage: {self.mileage} km\nVIN: {self.vin}\n"
        details += f"Engine: {self.engine}\nTransmission: {self.transmission}\nOptions: {', '.join(self.options)}"
        return details


class Car(Vehicle):
    def __init__(self, model_year, mileage, vin, engine, transmission, options, body_style, num_doors):
        """
        Initialize a Car, extending the Vehicle class.
        """
        super().__init__(model_year, mileage, vin, engine, transmission, options)
        self.body_style = body_style  # Example: Sedan, Coupe
        self.num_doors = num_doors  # Example: 2-door, 4-door

    def __str__(self):
        """
        String representation of a Car object.
        """
        details = super().__str__()
        details += f"\nBody Style: {self.body_style}\nNumber of Doors: {self.num_doors}"
        return details


class Truck(Vehicle):
    def __init__(self, model_year, mileage, vin, engine, transmission, options, payload_capacity, bed_length):
        """
        Initialize a Truck, extending the Vehicle class.
        """
        super().__init__(model_year, mileage, vin, engine, transmission, options)
        self.payload_capacity = payload_capacity  # Example: in kg
        self.bed_length = bed_length  # Example: in meters

    def __str__(self):
        """
        String representation of a Truck object.
        """
        details = super().__str__()
        details += f"\nPayload Capacity: {self.payload_capacity} kg\nBed Length: {self.bed_length} meters"
        return details


class SUV(Vehicle):
    def __init__(self, model_year, mileage, vin, engine, transmission, options, seating_capacity, is_all_wheel_drive):
        """
        Initialize an SUV, extending the Vehicle class.
        """
        super().__init__(model_year, mileage, vin, engine, transmission, options)
        self.seating_capacity = seating_capacity
        self.is_all_wheel_drive = is_all_wheel_drive

    def __str__(self):
        """
        String representation of an SUV object.
        """
        details = super().__str__()
        details += f"\nSeating Capacity: {self.seating_capacity}\nAll-Wheel Drive: {'Yes' if self.is_all_wheel_drive else 'No'}"
        return details


class Minivan(Vehicle):
    def __init__(self, model_year, mileage, vin, engine, transmission, options, sliding_doors, cargo_space):
        """
        Initialize a Minivan, extending the Vehicle class.
        """
        super().__init__(model_year, mileage, vin, engine, transmission, options)
        self.sliding_doors = sliding_doors  # Number of sliding doors
        self.cargo_space = cargo_space  # Cargo space in cubic meters

    def __str__(self):
        """
        String representation of a Minivan object.
        """
        details = super().__str__()
        details += f"\nSliding Doors: {self.sliding_doors}\nCargo Space: {self.cargo_space} cubic meters"
        return details


# Demonstration
if __name__ == "__main__":
    # Example instances
    car = Car(
        model_year=2020, mileage=15000, vin="1HGBH41JXMN109186",
        engine="2.0L I4", transmission="Automatic",
        options=["Cruise Control", "Bluetooth"], body_style="Sedan", num_doors=4
    )

    truck = Truck(
        model_year=2019, mileage=25000, vin="1FTFW1E53JKE37654",
        engine="3.5L V6", transmission="Manual",
        options=["Tow Package", "Backup Camera"], payload_capacity=2000, bed_length=2.5
    )

    suv = SUV(
        model_year=2021, mileage=12000, vin="5YJ3E1EB9KF317236",
        engine="Electric", transmission="Single Speed",
        options=["All-Terrain Tires", "Heated Seats"], seating_capacity=7, is_all_wheel_drive=True
    )

    minivan = Minivan(
        model_year=2018, mileage=30000, vin="2C4RC1BG5JR182406",
        engine="3.6L V6", transmission="Automatic",
        options=["DVD Player", "Remote Start"], sliding_doors=2, cargo_space=4.5
    )

    # Displaying the objects
    print("=== Car ===")
    print(car)
    print("\n=== Truck ===")
    print(truck)
    print("\n=== SUV ===")
    print(suv)
    print("\n=== Minivan ===")
    print(minivan)
