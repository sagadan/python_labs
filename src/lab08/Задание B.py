from models import Student


def students_to_json(students: list[Student], path: str):
    """
    Сериализация списка студентов в JSON файл

    Args:
        students: список объектов Student
        path: путь к файлу для сохранения
    """
    data = [student.to_dict() for student in students]

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> list[Student]:
    """
    Десериализация JSON файла в список студентов

    Args:
        path: путь к JSON файлу

    Returns:
        list[Student]: список объектов Student
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        students = []
        for item in data:
            try:
                student = Student.from_dict(item)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка при создании студента из данных: {item}. Ошибка: {e}")
                continue

        return students
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON файла {path}")
        return []


students_list = students_from_json('data/lab08/students_input.json')
for item in students_list:
    print(item)
