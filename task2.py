# ===== Задание 2: Система сотрудников =====

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} работает.")

    def get_info(self):
        return f"Сотрудник: {self.name}, зарплата: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def work(self):
        print(f"{self.name} управляет отделом: {self.department}")

    def hold_meeting(self):
        print(f"{self.name} проводит совещание с отделом {self.department}.")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def work(self):
        print(f"{self.name} пишет код на {self.programming_language}")

    def debug_code(self):
        print(f"{self.name} отлаживает код на {self.programming_language}")


# Демонстрация полиморфизма
employees = [
    Manager("Анна", 120000, "Продажи"),
    Developer("Сергей", 150000, "Python"),
]

for emp in employees:
    emp.work()     # Полиморфизм
    print(emp.get_info())
