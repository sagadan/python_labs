from datetime import datetime, date #работает с датой и временем
from dataclasses import dataclass # библиотека для сереализации (есть некий объект и хотим превратить в текст)

@dataclass # декоратор - это то что будет выполнено до исполнения(заранее)
class Student:
    """Класс Student представляет студента учебного заведения"""
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __init__(self, fio, birthdate, group, gpa):
        """Конструктор класса Student"""
        self.fio = fio
        self.birthdate = birthdate
        self.group = group
        self.gpa = gpa
        self.__post_init__()

    def __post_init__(self):
    # Проверяем, является ли birthdate строкой
        if isinstance(self.birthdate, str):
            try:
            # Если это строка, парсим ее
                self._date_of_birth = datetime.strptime(self.birthdate, '%Y-%m-%d')
            except ValueError:
                raise ValueError('Invalid date format. Expected YYYY-MM-DD')
        else:
        # Если это уже объект date, оставляем как есть
            self._date_of_birth = self.birthdate
        

    def age(self) -> int:
        """Рассчитывает возраст студента в полных годах"""
        b = self.birthdate ## birthdate теперь объект datetime после валидации
        today = date.today()
        if today.month > b.month:
            return today.year - b.year
        if today.month < b.month:
            return today.year - b.year - 1
        if today.day >= b.day:
            return today.year - b.year
        return today.year - b.year - 1

    def to_dict(self) -> dict:
        """ Сериализует объект Student в словарь
        (Словарь с данными студента, готовый для сохранения в JSON)"""
        
        return {
            "fio": self.fio,
            "birthdate": self.birthdate.strftime("%Y/%m/%d"),
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod 
    def from_dict(cls, d: dict):
        """Десериализует словарь в объект Student"""
        fio = d["fio"]
        birthdate = d["birthdate"]
        group = d["group"]
        gpa = d["gpa"]
        return cls(fio, birthdate, group, gpa)

    def __str__(self):
        """ Возвращает читаемое строковое представление объекта"""
        return f"Student:{self.fio}, {self.age()} years old, group {self.group}, rating {self.gpa}"
    