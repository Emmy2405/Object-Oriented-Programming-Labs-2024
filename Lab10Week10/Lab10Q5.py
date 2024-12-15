class Student:
    """
    Represents a student with details such as study type, first name, last name, and registered courses.
    """

    UNDERGRADUATE = "Undergraduate"
    POSTGRADUATE = "Postgraduate"

    def __init__(self, study_type, f_name, l_name):
        """
        Initialize a Student instance.
        :param study_type: Type of study (e.g., "Undergraduate" or "Postgraduate").
        :param f_name: First name of the student.
        :param l_name: Last name of the student.
        """
        self.study_type = study_type
        self.f_name = f_name
        self.l_name = l_name
        self.courses = []  # List to store registered courses

    def set_courses(self, course):
        """
        Add a course to the student's list of registered courses.
        :param course: Course name to add.
        """
        self.courses.append(course)

    def __str__(self):
        """
        String representation of the student object.
        """
        courses = ", ".join(self.courses) if self.courses else "No courses registered"
        return (f"Student Name: {self.f_name} {self.l_name}\n"
                f"Study Type: {self.study_type}\n"
                f"Registered Courses: {courses}")


class RegistrationData:
    """
    Represents the registration data for a student, including address, fee, and a linked Student object.
    """

    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        """
        Initialize a RegistrationData instance.
        :param address: Address of the student.
        :param registration_fee: Registration fee.
        :param study_type: Type of study (e.g., "Undergraduate" or "Postgraduate").
        :param f_name: First name of the student.
        :param l_name: Last name of the student.
        :param s_id: Student ID (default is "NA").
        """
        self.address = address
        self.registration_fee = registration_fee
        self.student = Student(study_type, f_name, l_name)
        self.student_id = s_id

    def set_student_id_property(self, s_id):
        """
        Set the student ID for the registration.
        :param s_id: Student ID to set.
        """
        self.student_id = s_id

    def get_student_object(self):
        """
        Get the linked Student object.
        :return: The Student object.
        """
        return self.student

    def display_student_data(self):
        """
        Display student data including registration details.
        """
        print(f"Address: {self.address}\n"
              f"Registration Fee: {self.registration_fee}\n"
              f"Student ID: {self.student_id}\n"
              f"{self.student}")


# MAIN SCOPE - UNCOMMENT IT AND RUN AFTER IMPLEMENTING YOUR SOLUTION
r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                     Student.POSTGRADUATE, "Lucas", "Rizzo")
r.display_student_data()
print()
r.set_student_id_property("C12345")
r.display_student_data()
print()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.get_student_object().set_courses(course)

r.display_student_data()
print()
print(r.get_student_object())  # extra to match the __str__ additional function
print()
print(RegistrationData.__doc__)
