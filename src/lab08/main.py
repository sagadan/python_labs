from serialize import students_from_json, students_to_json
from models import Student

def main():
    s1 = Student("Michael Jackson","1958-08-29", "MJ-01", 3.6)
    s2 = Student("Brad Pitt","1963-12-18", "BP-09", 4.2)
    s3 = Student("Will Smith","1968-09-25", "WS-43", 5.0)
    # Преобразуем список объектов в JSON файл
    students_to_json([s1,s2,s3], "/Applications/python_labs/data/lab08/students_output.json")
    for s in students_from_json("/Applications/python_labs/data/lab08/students_input.json"):
        #Загружаем данные из JSON файла и создаем объекты
        print(s)

if __name__ == '__main__':
    main()