#!/usr/bin/env python3
import sys
import os

# Добавляем корень проекта в путь Python
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from datetime import date

# Импортируем Group
from group import Group

# Простой класс Student для тестирования
class Student:
    def __init__(self, fio: str, birthdate: date, group: str, gpa: float):
        self.fio = fio
        self.birthdate = birthdate
        self.group = group
        self.gpa = float(gpa)

def main():
    print("Тестирование класса Group")
    
    # Указываем путь к CSV файлу
    csv_path = os.path.join(project_root, 'data/lab09/students (1).csv')
    print(f"Используем файл: {csv_path}")
    
    # Создаем директорию, если ее нет
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    
    # Создаем группу
    group = Group(csv_path)
    
    # 1. Добавление студентов
    print("\n1. Добавление студентов:")
    try:
        student1 = Student("Романов Иван Алексеевич", date(2003, 10, 10), "БИВТ-21-1", 4.3)
        student2 = Student("Шкалова Анна Васильевна", date(2002, 5, 15), "БИВТ-21-1", 4.7)
        student3 = Student("Кирилов Алексей Романович", date(2003, 3, 20), "БИВТ-21-2", 3.8)
        
        group.add(student1)
        group.add(student2)
        group.add(student3)
        print("   Студенты успешно добавлены")
    except ValueError as e:
        print(f"   Ошибка при добавлении: {e}")
    
    # 2. Вывод списка всех студентов
    print("\n2. Все студенты:")
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"   {i}. {student.fio}, {student.birthdate}, {student.group}, {student.gpa}")
    
    # 3. Поиск студентов
    print("\n3. Поиск студентов с 'Иван':")
    found = group.find("Иван")
    for i, student in enumerate(found, 1):
        print(f"   {i}. {student.fio}, {student.birthdate}, {student.group}, {student.gpa}")
    
    # 4. Обновление студента
    print("\n4. Обновление данных студента:")
    try:
        group.update("Иванов Иван Иванович", gpa=4.5, group="БИВТ-21-3")
        print("   Данные студента обновлены")
    except ValueError as e:
        print(f"   Ошибка при обновлении: {e}")
    
    # 5. Проверка после обновления
    print("\n5. Студенты после обновления:")
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"   {i}. {student.fio}, {student.group}, GPA: {student.gpa}")
    
    # 6. Удаление студента
    print("\n6. Удаление студента:")
    group.remove("Петрова Анна Сергеевна")
    
    # 7. Финальный список
    print("\n7. Финальный список студентов:")
    all_students = group.list()
    if all_students:
        for i, student in enumerate(all_students, 1):
            print(f"   {i}. {student.fio}, {student.group}, GPA: {student.gpa}")
    else:
        print("   Нет студентов")

if __name__ == "__main__":
    main()