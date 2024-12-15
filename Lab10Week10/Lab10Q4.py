class Member:
    def __init__(self, name, age, membership_type):
        """
        Initialize a Member instance.
        :param name: Name of the member.
        :param age: Age of the member.
        :param membership_type: Type of membership (e.g., "Basic", "Premium").
        """
        self.name = name
        self.age = age
        self.membership_type = membership_type

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Membership Type: {self.membership_type}"


class Equipment:
    def __init__(self, name, quantity):
        """
        Initialize an Equipment instance.
        :param name: Name of the equipment.
        :param quantity: Quantity available in the gym.
        """
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Equipment: {self.name}, Quantity: {self.quantity}"


class Gym:
    def __init__(self, name):
        """
        Initialize a Gym instance.
        :param name: Name of the gym.
        """
        self.name = name
        self.members = []  # List to store members
        self.equipment = []  # List to store equipment

    def add_member(self, member):
        """
        Add a new member to the gym.
        :param member: An instance of the Member class.
        """
        self.members.append(member)
        print(f"Added member: {member.name}")

    def add_equipment(self, equipment):
        """
        Add new equipment to the gym.
        :param equipment: An instance of the Equipment class.
        """
        self.equipment.append(equipment)
        print(f"Added equipment: {equipment.name}")

    def list_members(self):
        """List all the members in the gym."""
        print(f"Members of {self.name}:")
        for member in self.members:
            print(member)

    def list_equipment(self):
        """List all the equipment in the gym."""
        print(f"Equipment in {self.name}:")
        for eq in self.equipment:
            print(eq)

    def __str__(self):
        return f"Gym Name: {self.name}, Members: {len(self.members)}, Equipment: {len(self.equipment)}"


# Main Program
if __name__ == "__main__":
    # Create a gym
    gym = Gym("Iron Paradise")

    # Create members
    member1 = Member("John Doe", 30, "Basic")
    member2 = Member("Jane Smith", 25, "Premium")
    member3 = Member("Alice Johnson", 35, "Premium")

    # Add members to the gym
    gym.add_member(member1)
    gym.add_member(member2)
    gym.add_member(member3)

    # Create equipment
    equipment1 = Equipment("Treadmill", 5)
    equipment2 = Equipment("Dumbbells", 20)
    equipment3 = Equipment("Bench Press", 2)

    # Add equipment to the gym
    gym.add_equipment(equipment1)
    gym.add_equipment(equipment2)
    gym.add_equipment(equipment3)

    # Display gym details
    print("\nGym Details:")
    print(gym)

    # List all members
    print("\nListing Members:")
    gym.list_members()

    # List all equipment
    print("\nListing Equipment:")
    gym.list_equipment()
