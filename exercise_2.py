# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші.
# Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.
"""exercise 2"""
import random


class Rectangle:
    """Create class Rectangle"""

    def __init__(self, name, height, width, color):
        self.name = name
        self.height = height
        self.width = width
        self.color = color
        print("---Вікно викликане---")

    def change_color(self):
        """Change color rectangle"""
        color_list = [
            "білий",
            "сріблястий",
            "чорний",
            "сірий",
            "червоний",
            "коричневий",
            "синій",
            "зелений",
            "золотистий",
        ]
        self.color = random.choice(color_list)
        print(f"Колір вікна був змінений на {self.color}")

    def info(self):
        """Print info about rectangle"""
        print(
            f"Інформація про створенно вікно:\n"
            f"Назва: {self.name} \n"
            f"Высота: {self.height}\n"
            f"Ширина: {self.width}\n"
            f"Колір: {self.color}\n"
        )


class Button:
    """Create button for work rectangle"""

    @staticmethod
    def button_change_color():
        """Call function change_colorin rectangle"""
        window.change_color()

    @staticmethod
    def button_info():
        """Call function info in rectangle"""
        window.info()


class Mouse:
    """Create mouse for choice buttons"""

    def __init__(self, position):
        self.position = position

    def change_position(self, new_position):
        """Change choice position buttons"""
        self.position = new_position
        if new_position == "1":
            print("Ви навели мишку на кнопку 1")
        elif new_position == "2":
            print("Ви навели мишку на кнопку 2")
        else:
            print("Такої кнопки не інує. Повторіть спробу")

    def click(self):
        """Simulation click mouse"""
        if self.position == "1":
            button_1.button_change_color()
        elif self.position == "2":
            button_2.button_info()


# Start window, button and mouse
window = Rectangle("ITVDN", 300, 300, "зелений")
button_1 = Button()
button_2 = Button()
mouse = Mouse(None)

while True:
    commond = input(
        "Натисніть 1, щоб навести мишку на кнопку 1 яка змінює колір вікна.\n"
        "Натисніть 2, щоб навести мишку на кнопку 2 яка змінює виводить інформацію про вікно.\n"
        "Для того щоб зробити клік, відправте пустий рядок\n"
    )
    if (commond == "") and (mouse.position is None):
        print("Ви не навели мишку на кнопку!!! \n")
        continue
    elif commond == "":
        mouse.click()
    else:
        mouse.change_position(commond)
    print()
