from datetime import date


class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    @staticmethod
    def is_adult_ukraine(age):
        print("Є повнолітнім в Україні" if age >= 18 else "Не є повнолітнім в Україні")

    @staticmethod
    def is_adult_america(age):
        print("Є повнолітнім в Америці" if age >= 21 else "Не є повнолітнім в Америці")

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    color = 'White'


print("Перевірка по Україні")
MyClass1.is_adult_ukraine(17)
MyClass1.is_adult_ukraine(18)
MyClass1.is_adult_ukraine(20)

print("Перевірка по США")
MyClass1.is_adult_america(17)
MyClass1.is_adult_america(20)
MyClass1.is_adult_america(22)