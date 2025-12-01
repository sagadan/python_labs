import json
from typing import List
from models import Student  


def students_to_json(students: List[Student], path: str) -> None:

    data_to_save = []
    for student in students:
        data_to_save.append(student.to_dict())
    
    # Открываем файл и записываем
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data_to_save, file, ensure_ascii=False, indent=2)
    
    print(f"Успешно сохранили {len(students)} студентов в {path}")


def students_from_json(path: str) -> List[Student]:

    students = []
    
    try:
        # Читаем файл
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # ← ТУТ тоже используется json!
        
        # Создаем студентов из данных
        for item in data:
            try:
                student = Student.from_dict(item)
                students.append(student)
            except Exception as e:
                print(f"Не удалось создать студента: {item.get('fio', 'Без имени')}")
                print(f"Ошибка: {e}")
                continue
        
        print(f"Загрузили {len(students)} студентов из {path}")
        
    except FileNotFoundError:
        print(f"Файл {path} не найден!")
    except json.JSONDecodeError:  # ← ТЕПЕРЬ json определен!
        print(f"Файл {path} поврежден или не в JSON формате!")
    
    return students


student1 = Student("Лимонов Максим", "2002-10-30", "ИВТ-104", 4.2)
student2 = Student("Апельсинова Юля", "2003-02-01", "ИВТ-105", 3.8)

# Проверяем возраст
print(f"{student1.fio}: {student1.age()} лет")  # Выведет: Иванов Иван: 21 лет

# Сохраняем в файл
students_to_json([student1, student2], "/Applications/python_labs/src/lab08/students.json")

# Загружаем обратно
loaded_students = students_from_json("/Applications/python_labs/src/lab08/students.json")

# Используем загруженных
for student in loaded_students:
    print(student)  # Вызовется student.__str__()