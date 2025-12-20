class Person:
    def __init__(self, name, address, age):
        self._name = name
        self.address = address
        self.age = age

    def greet(self):
        print("Greetings and felicitations from the maestro " + self._name)
