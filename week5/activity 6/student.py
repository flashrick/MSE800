from person import Person


class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id

    # The output is different from the inherited greet() method because the method has been overridden in the subclass.
    def greet(self):
        print("Hi " + self._name)


# Test
student1 = Student("Alice", "123 Main St", 20, "S12345")
student1.greet()
