# Створіть ієрархію класів із використанням множинного успадкування. Виведіть на екран порядок вирішення методів
# для кожного класу. Поясніть, чому лінеаризація даних класів виглядає саме так.
"""exercise 3"""


class Animals:
    """Створення класу Animals"""

    def __init__(self, animal_breed, age):
        self.animal_breed = animal_breed
        self.age = age

    def animal_info(self):
        """Виведення інформації про істоту"""
        print(f"Тварина виду: {self.animal_breed} віком {self.age}")


class Birds(Animals):
    """Створення класу Birds на основі класу Animals"""


    @staticmethod
    def can_fly():
        """Виведення інформації, що істота може літати"""
        print("Істота може літати")


class Beasts(Animals):
    """Створення класу Вeasts на основі класу Animals"""


    @staticmethod
    def can_drink_milk():
        """Виведення інформації, що істота може пити молоко"""
        print("Істота може пити молоко")


class Fish(Animals):
    """Створення класу Fish на основі класу Animals"""

    @staticmethod
    def can_swim():
        """Виведення інформації, що істота може пити плавати"""
        print("Істота може плавати")


class Dolphins(Fish, Beasts):
    """Створення класу Dolphins на основі класів Fish, Вeasts"""

    def __init__(self, animal_breed, age):
        Animals.__init__(self, animal_breed, age)


class Bats(Birds, Beasts):
    """Створення класу Dolphins на основі класів Birds, Вeasts"""

    def __init__(self, animal_breed, age):
        Animals.__init__(self, animal_breed, age)


# Створюємо дельфіна і перевіряеємо його методи
# Дельфін наслідується від звірів (Вeasts) та риб (Fish)
dolphin = Dolphins("Дельфін", 10)
dolphin.animal_info()
dolphin.can_swim()
dolphin.can_drink_milk()
print(Dolphins.mro())
# Найстарший клас object від якого наслідуються всі інші методи користувацькі методи. Далі іде Animals, який має
# під класи Вeasts та Fish. На основі классів Вeasts та Birds було створенно Dolphins
# Лінерізація іде снизу до гори, та зліва направо.
# Dolphins --> Fish, Вeasts (послідовність як при ініціалізації) --> Animals --> object

print()

# Створюємо кажана і перевіряеємо його методи
# Кажан наслідується від звірів (Вeasts) та птиць (Birds)
bat = Bats("Кажан", 1)
bat.animal_info()
bat.can_fly()
bat.can_drink_milk()

print(Bats.mro())
# Найстарший клас object від якого наслідуються всі інші методи користувацькі методи. Далі іде Animals, який має
# під класи Вeasts та Birds. На основі классів Вeasts та Birds було створенно Bats
# Лінерізація іде снизу до гори, та зліва направо.
# Bats --> Birds, Вeasts (послідовність як при ініціалізації) --> Animals --> object
