class Person:
    def __init__(self, name, age, ssn):
        # self.name = name #public attribute
        self._name = name #public attribute
        self._age = age #protected attribute
        self.__ssn = ssn #private attribute
    # Getter for the name
    def get_name(self):
        return self._name
    # Setter for name
    def set_name(self, value):
        if isinstance(value, str) and value.isalpha():
            self.name = value
        else:
            raise ValueError("Name must be a string and containing only letters!")
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if 0<value<120:
            self._age = value
        else:
            raise ValueError("Age must be between 1 and 119")

person = Person("David", 20, "123-14-5454")
# print(person.name) #output: David
# print(person._age) #(accessible)
# # print(person.__ssn) #attribute error
# print(person._Person__ssn)

print(person.get_name())
person.set_name("Aisha")
print(person.get_name())
person.age = 119

