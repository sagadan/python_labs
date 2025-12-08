import csv
import sys, os
from pathlib import Path
from typing import List, Optional
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lab08')))
from models import Student


class Group:
    """Класс для управления студентами в CSV-файле"""
    
    def __init__(self, storage_path: str):
        """
        Инициализация группы.
        
        Args:
            storage_path: путь к CSV-файлу
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        """Создает файл с заголовком, если он не существует"""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
    
    def _read_all(self) -> List[dict]:
        """Чтение всех записей из CSV-файла"""
        if not self.path.exists():
            return []
        
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _write_all(self, rows: List[dict]) -> None:
        """Запись всех записей в CSV-файл"""
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)
    
    def _convert_to_student(self, row: dict) -> Student:
        """Конвертация словаря в объект Student"""
        return Student(
            fio=row['fio'],
            birthdate=datetime.strptime(row['birthdate'], '%Y-%m-%d').date(),
            group=row['group'],
            gpa=float(row['gpa'])
        )
    
    def _convert_from_student(self, student: Student) -> dict:
        """Конвертация объекта Student в словарь"""
        return {
            'fio': student.fio,
            'birthdate': student.birthdate.isoformat(),
            'group': student.group,
            'gpa': str(student.gpa)
        }
    
    def list(self) -> List[Student]:
        """
        Получить всех студентов.
        
        Returns:
            Список объектов Student
        """
        rows = self._read_all()
        students = []
        
        for row in rows:
            try:
                student = self._convert_to_student(row)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка конвертации строки {row}: {e}")
                continue
        
        return students
    
    def add(self, student: Student) -> None:
        """
        Добавить нового студента.
        
        Args:
            student: объект Student для добавления
        """
        rows = self._read_all()
        
        # Проверяем, нет ли уже студента с таким ФИО
        for row in rows:
            if row['fio'] == student.fio:
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")
        
        # Добавляем нового студента
        rows.append(self._convert_from_student(student))
        self._write_all(rows)
    
    def find(self, substr: str) -> List[Student]:
        """
        Поиск студентов по подстроке в ФИО.
        
        Args:
            substr: подстрока для поиска в ФИО
            
        Returns:
            Список найденных студентов
        """
        all_students = self.list()
        found = []
        
        for student in all_students:
            if substr.lower() in student.fio.lower():
                found.append(student)
        
        return found
    
    def remove(self, fio: str) -> bool:
        """
        Удалить студента по ФИО.
        
        Args:
            fio: ФИО студента для удаления
            
        Returns:
            True если студент был удален, False если не найден
        """
        rows = self._read_all()
        original_count = len(rows)
        
        # Удаляем все записи с указанным ФИО
        rows = [row for row in rows if row['fio'] != fio]
        
        if len(rows) < original_count:
            self._write_all(rows)
            return True
        return False
    
    def update(self, fio: str, **fields) -> bool:
        """
        Обновить поля существующего студента.
        
        Args:
            fio: ФИО студента для обновления
            **fields: поля для обновления (fio, birthdate, group, gpa)
            
        Returns:
            True если студент был обновлен, False если не найден
        """
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                # Обновляем указанные поля
                for key, value in fields.items():
                    if key in row:
                        if key == 'birthdate' and hasattr(value, 'isoformat'):
                            row[key] = value.isoformat()
                        elif key == 'gpa':
                            row[key] = str(float(value))
                        else:
                            row[key] = str(value)
                updated = True
                break
        
        if updated:
            self._write_all(rows)
        
        return updated
    
    def stats(self) -> dict:
        """
        Получить статистику по группе.
        
        Returns:
            Словарь со статистикой
        """
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }
        
        gpas = [student.gpa for student in students]
        groups_dict = {}
        
        for student in students:
            group = student.group
            groups_dict[group] = groups_dict.get(group, 0) + 1
        
        # Сортируем студентов по GPA (по убыванию)
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        
        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups_dict,
            "top_5_students": [
                {"fio": s.fio, "gpa": s.gpa} 
                for s in sorted_students[:5]
            ]
        }
    
    def print_all(self) -> None:
        """Вывести всех студентов в читаемом формате"""
        students = self.list()
        
        if not students:
            print("Нет студентов в базе")
            return
        
        print(f"{'ФИО':<30} {'Дата рождения':<15} {'Группа':<15} {'GPA':<5}")
        print("-" * 70)
        
        for student in students:
            print(f"{student.fio:<30} {student.birthdate:<15} {student.group:<15} {student.gpa:<5.2f}")





