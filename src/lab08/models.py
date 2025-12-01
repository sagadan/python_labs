from dataclasses import dataclass, asdict, field
from datetime import datetime, date
from typing import ClassVar
import re


@dataclass
class Student:

    fio: str
    birthdate: str
    group: str
    gpa: float

    # Паттерн для проверки формата даты
    DATE_PATTERN: ClassVar[str] = r'^\d{4}-\d{2}-\d{2}$'

    def __post_init__(self):
        self._validate_birthdate()
        self._validate_gpa()

    def _validate_birthdate(self):
        if not re.match(self.DATE_PATTERN, self.birthdate):
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается: YYYY-MM-DD")

        # Проверка, что дата является корректной
        try:
            year, month, day = map(int, self.birthdate.split('-'))
            date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Некорректная дата: {self.birthdate}. Ошибка: {e}")

    def _validate_gpa(self):
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Средний балл должен быть в диапазоне 0-5. Получено: {self.gpa}")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()

        # Вычисляем возраст
        age = today.year - birth_date.year

        # Корректируем, если день рождения в этом году еще не наступил
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )

    def __str__(self) -> str:
        return (f"Студент: {self.fio}\n"
                f"Дата рождения: {self.birthdate} (Возраст: {self.age()} лет)\n"
                f"Группа: {self.group}\n"
                f"Средний балл: {self.gpa:.2f}")