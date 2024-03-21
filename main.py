import math


class Person:
    """
    Реалізує клас «Людина» з ім'ям, віком та статтю.
    """

    __instances_count = 0

    def __init__(self, name: str, age: int, gender: str):
        """
        Ініціалізація екземпляра класу «Людина».

        Аргументи:
            name: Ім'я людини.
            age: Вік людини.
            gender: Стать людини.
        """
        self.__name = name
        self.__age = age
        self.__gender = gender

        Person.__instances_count += 1

    @staticmethod
    def get_total_instances() -> int:
        """
        Повертає загальну кількість створених екземплярів класу «Людина».

        Повертає:
            Кількість екземплярів.
        """
        return Person.__instances_count

    def __str__(self):
        """
        Повертає рядок з інформацією про людину.
        """
        return f"""
        **Ім'я:** {self.__name}
        **Вік:** {self.__age} років
        **Стать:** {self.__gender}
        """


person1 = Person("Іван", 25, "чоловіча")
person2 = Person("Марія", 30, "жіноча")

print(f"Кількість людей: {Person.get_total_instances()}")  # 2

print(person1)
print(person2)


# Завдання 2
class AreaCalculator:
    """
    Реалізує клас для підрахунку площі геометричних фігур.
    """

    __total_calculations = 0

    @staticmethod
    def calculate_triangle_area_heron(a: float, b: float, c: float) -> float:
        """
        Розраховує площу трикутника за формулою Герона.

        Аргументи:
            a: Довжина першої сторони трикутника.
            b: Довжина другої сторони трикутника.
            c: Довжина третьої сторони трикутника.

        Повертає:
            Площа трикутника.
        """
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        AreaCalculator.__total_calculations += 1
        return area

    @staticmethod
    def calculate_triangle_area_base_height(base: float, height: float) -> float:
        """
        Розраховує площу трикутника за основою та висотою.

        Аргументи:
            base: Довжина основи трикутника.
            height: Висота трикутника.

        Повертає:
            Площа трикутника.
        """
        area = 0.5 * base * height
        AreaCalculator.__total_calculations += 1
        return area

    @staticmethod
    def calculate_triangle_area_sides_angle(a: float, b: float, angle: float) -> float:
        """
        Розраховує площу трикутника за двома сторонами та кутом між ними.

        Аргументи:
            a: Довжина першої сторони трикутника.
            b: Довжина другої сторони трикутника.
            angle: Кут між сторонами a і b (в градусах).

        Повертає:
            Площа трикутника.
        """
        area = 0.5 * a * b * math.sin(angle * math.pi / 180)
        AreaCalculator.__total_calculations += 1
        return area

    @staticmethod
    def calculate_rectangle_area(width: float, height: float) -> float:
        """
        Розраховує площу прямокутника.

        Аргументи:
            width: Ширина прямокутника.
            height: Висота прямокутника.

        Повертає:
            Площа прямокутника.
        """
        area = width * height
        AreaCalculator.__total_calculations += 1
        return area

    @staticmethod
    def calculate_square_area(side: float) -> float:
        """
        Розраховує площу квадрата.

        Аргументи:
            side: Довжина сторони квадрата.

        Повертає:
            Площа квадрата.
        """
        return AreaCalculator.calculate_rectangle_area(side, side)

    @staticmethod
    def calculate_rhombus_area(diagonal1: float, diagonal2: float) -> float:
        """
        Розраховує площу ромба.

        Аргументи:
            diagonal1: Довжина першої діагоналі ромба.
            diagonal2: Довжина другої діагоналі ромба.

        Повертає:
            Площа ромба.
        """
        area = 0.5 * diagonal1 * diagonal2
        AreaCalculator.__total_calculations += 1
        return area

    @staticmethod
    def get_total_calculations() -> int:
        """
        Повертає загальну кількість виконаних розрахунків площі.

        Повертає:
            Кількість розрахунків.
        """
        return AreaCalculator.__total_calculations


triangle_area_heron = AreaCalculator.calculate_triangle_area_heron(3, 4, 5)
print(f"Площа трикутника за формулою Герона: {triangle_area_heron:.2f}")

rectangle_area = AreaCalculator.calculate_rectangle_area(5, 7)
print(f"Площа прямокутника: {rectangle_area:.2f}")

area_by_height = AreaCalculator.calculate_triangle_area_base_height(6, 7)
print(f"Розраховує площу трикутника за основою та висотою: {area_by_height:.2f}")

square_on_two_sides = AreaCalculator.calculate_triangle_area_sides_angle(5, 6, 7)
print(f"Розраховує площу трикутника за двома сторонами та кутом між ними: {square_on_two_sides:.2f}")

area_of_a_square = AreaCalculator.calculate_square_area(4)
print(f"Площа квадрата: {area_of_a_square:.2f}")

rhombus_area = AreaCalculator.calculate_rhombus_area(6, 7)
print(f"Площа ромба: {rhombus_area:.2f}")

total_calculations = AreaCalculator.get_total_calculations()
print(f"Кількість виконаних розрахунків площі: {total_calculations:.2f}")


# Завдання 3
class MathOperations:
    """
    Реалізує клас для виконання математичних операцій з 4 аргументами.
    """

    @staticmethod
    def find_max(a: float, b: float, c: float, d: float) -> float:
        """
        Повертає максимальне значення з 4 чисел.

        Аргументи:
            a: Перше число.
            b: Друге число.
            c: Третє число.
            d: Четверте число.

        Повертає:
            Максимальне значення.
        """
        return max(a, b, c, d)

    @staticmethod
    def find_min(a: float, b: float, c: float, d: float) -> float:
        """
        Повертає мінімальне значення з 4 чисел.

        Аргументи:
            a: Перше число.
            b: Друге число.
            c: Третє число.
            d: Четверте число.

        Повертає:
            Мінімальне значення.
        """
        return min(a, b, c, d)

    @staticmethod
    def calculate_average(a: float, b: float, c: float, d: float) -> float:
        """
        Повертає середнє арифметичне 4 чисел.

        Аргументи:
            a: Перше число.
            b: Друге число.
            c: Третє число.
            d: Четверте число.

        Повертає:
            Середнє арифметичне.
        """
        return (a + b + c + d) / 4

    @staticmethod
    def calculate_factorial(n: int) -> int:
        """
        Повертає факторіал числа.

        Аргументи:
            n: Ціле число.

        Повертає:
            Факторіал числа.
        """
        if n < 0:
            raise ValueError("Не можна обчислити факторіал від'ємного числа")
        if n == 0 or n == 1:
            return 1
        else:
            return n * MathOperations.calculate_factorial(n - 1)


max_value = MathOperations.find_max(10, 2, 5, 15)
print(f"Максимальне значення: {max_value}")

min_value = MathOperations.find_min(10, 2, 5, 15)
print(f"Мінімальне значення: {min_value}")

average_value = MathOperations.calculate_average(10, 2, 5, 15)
print(f"Середнє арифметичне: {average_value}")

factorial_value = MathOperations.calculate_factorial(5)
print(f"Факторіал числа 5: {factorial_value}")

try:
    factorial_value = MathOperations.calculate_factorial(-5)
except ValueError as e:
    print(e)


# Завдання 4
class FileUtils:
    """
    Реалізує клас для підрахунку рядків у файлі.
    """

    @staticmethod
    def count_lines(file_path: str) -> int:
        """
        Підраховує та повертає кількість рядків у файлі.

        Аргументи:
            file_path: Шлях до файлу.

        Повертає:
            Кількість рядків у файлі.
        """
        try:
            with open(file_path, "r") as f:
                lines = f.readlines()
            return len(lines)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не знайдено: {file_path}")


file_path = "1.txt"
line_count = FileUtils.count_lines(file_path)
print(f"Кількість рядків у файлі: {line_count}")

try:
    file_path = "2.txt"
    line_count = FileUtils.count_lines(file_path)
except FileNotFoundError as e:
    print(e)


# Завдання 5
class Character:
    """
    Реалізує клас для опису ігрового персона.
    """

    def __init__(self, name: str, health: int, damage: int):
        """
        Ініціалізація екземпляра класу Character.

        Аргументи:
            name: Ім'я персонажа.
            health: Кількість одиниць здоров'я.
            damage: Кількість одиниць шкоди, яку завдає персонаж.
        """
        self.name = name
        self.health = health
        self.damage = damage

    @staticmethod
    def attack(attacker_name: str, target_name: str):
        """
        Виводить повідомлення про атаку гравця.

        Аргументи:
            attacker_name: Ім'я персонажа, який атакує.
            target_name: Ім'я персонажа, який зазнає атаки.
        """
        print(f"{attacker_name} атакує {target_name}!")

    @staticmethod
    def attack2(attacker: "Character", target: "Character"):
        """
        Виводить повідомлення про атаку гравця з інформацією про
        залишок
        здоров'я
        цілі.

        Аргументи:
            attacker: Екземпляр класу Character, який атакує.
            target: Екземпляр класу Character, який зазнає атаки.
        """
        print(f"{attacker.name} атакує {target.name}!")
        target.health -= attacker.damage
        print(f"{target.name} отримав {attacker.damage} шкоди!")
        print(f"Залишок здоров'я {target.name}: {target.health}")


player1 = Character("Ksu", 100, 20)
player2 = Character("Frezzy", 80, 15)

player1.attack2(player1, player2)


# Завдання 6
class Student:
    """
    Реалізує клас для опису студента.
    """

    def __init__(self, name: str, age: int, grade: float, courses: list):
        """
        Ініціалізація екземпляра класу Student.

        Аргументи:
            name: Ім'я студента.
            age: Вік студента.
            grade: Поточний бал студента.
            courses: Список предметів, які вивчає студент.
        """
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = courses

    @staticmethod
    def add_course(student: "Student", course_name: str):
        """
        Додає новий предмет до списку курсів студента.

        Аргументи:
            student: Екземпляр класу Student.
            course_name: Назва нового предмета.
        """
        if course_name not in student.courses:
            student.courses.append(course_name)
            print(f"Предмет {course_name} успішно додано!")
        else:
            print(f"Студент {student.name} вже вивчає предмет {course_name}")


student1 = Student("Ivan", 20, 4.5, ["Python", "Java"])

student1.add_course(student1, "Data Science")
student1.add_course(student1, "Python")

print(f"Список предметів {student1.name}: {student1.courses}")
