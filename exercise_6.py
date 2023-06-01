from datetime import date


class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    total_adults_ukraine = 0
    total_adults_america = 0

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    @staticmethod
    def is_adult_ukraine(age):
        print("Є повнолітнім в Україні" if age >= 18 else "Не є повнолітнім в Україні")

    @staticmethod
    def is_adult_america(age):
        print("Є повнолітнім в Америці" if age >= 21 else "Не є повнолітнім в Америці")

    @classmethod
    def count_adults_ukraine(cls, age):
        if age >= 18:
            cls.total_adults_ukraine += 1

    @classmethod
    def count_adults_america(cls, age):
        if age >= 21:
            cls.total_adults_america += 1

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    color = 'White'


MyClass1_1 = MyClass1("John", "Petrenko", 25)
MyClass1_2 = MyClass1("Anna", "Petrenko", 17)

MyClass1.count_adults_ukraine(MyClass1_1.age)
MyClass1.count_adults_ukraine(MyClass1_2.age)

MyClass1.count_adults_america(MyClass1_1.age)
MyClass1.count_adults_america(MyClass1_2.age)

print("Україна:")
print(f"Кількість повнолітніх осіб: {MyClass1.total_adults_ukraine}")

print("\nАмерика:")
print(f"Кількість повнолітніх осіб: {MyClass1.total_adults_america}")
