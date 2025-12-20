# Base class
class Person:
    def __init__(self, id: int, name: str):
        self.id = id  # unique identifier
        self.name = name  # display name


# Inherited class from Person
class Student(Person):
    def __init__(self, id: int, name: str, student_id: str):
        super().__init__(id, name)
        self.student_id = student_id  # student specific id


# Inherited class from Person
class Staff(Person):
    def __init__(self, id: int, name: str, staff_id: str, tax_num: str):
        super().__init__(id, name)
        self.staff_id = staff_id  # staff id
        self.tax_num = tax_num  # tax tracking number


# Inherited class from Staff
class General(Staff):
    def __init__(
        self, id: int, name: str, staff_id: str, tax_num: str, rate_of_pay: float
    ):
        super().__init__(id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay  # hourly pay rate


# Inherited class from Staff
class Academic(Staff):
    def __init__(
        self, id: int, name: str, staff_id: str, tax_num: str, publications: list[str]
    ):
        super().__init__(id, name, staff_id, tax_num)
        self.publications = publications  # list of published works


def main():
    student = Student(1, "Alice", "S12345")  # demo student instance
    general_staff = General(2, "Bob", "G67890", "T11111", 25.0)  # demo general staff
    academic_staff = Academic(
        3, "Charlie", "A54321", "T22222", ["Paper1", "Paper2"]
    )  # demo academic

    print(f"Student: {student.name}, ID: {student.student_id}")  # show student summary
    print(
        f"General Staff: {general_staff.name}, Rate of Pay: {general_staff.rate_of_pay}"
    )  # show general staff summary
    print(
        f"Academic Staff: {academic_staff.name}, Publications: {', '.join(academic_staff.publications)}"
    )  # show academic staff summary


if __name__ == "__main__":
    main()
