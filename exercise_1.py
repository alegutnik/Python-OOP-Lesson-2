# Створіть клас Editor, який містить методи view_document та edit_document. Нехай метод edit_document виводить на екран
# інформацію про те, що редагування документів недоступне для безкоштовної версії. Створіть підклас ProEditor, у якому
# цей метод буде перевизначено. Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу
# ProEditor, інакше Editor. Викликайте методи перегляду та редагування документів.
"""exercise 1"""


class Editor:
    """Create class Editor"""

    @staticmethod
    def view_document():
        """Print information about view permission"""
        print("Ви маєете доступ до перегляду документів")

    @staticmethod
    def edit_document():
        """Print information about edit permission"""
        print("Редагування документів недоступне для безкоштовної версії")


class ProEditor(Editor):
    """Create class ProEditor"""

    def __init__(self, key):
        self.key = key
        print(
            "Ліцензійний ключ вірний"
            if key == "1234"
            else "Ліцензійний ключ не вірний!!!"
        )

    @staticmethod
    def edit_document():
        """Key verification"""
        if key == "1234":
            print("Редагування документів доступне")
        else:
            super().edit_document()


# Example with Editor

file_1 = Editor
file_1.view_document()
file_1.edit_document()
print()

# Example with ProEditor

key = input("Для використання версії PRO введіть ліцензійний ключ: ")  # key = 1234
file_2 = ProEditor(key)
file_2.view_document()
file_2.edit_document()
