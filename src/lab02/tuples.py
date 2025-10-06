def format_name(name: str) -> str:
    fio = name.split()
    if len(fio) == 3:
        last_name = fio[0].capitalize().strip()
        first_name = fio[1][0].upper().strip()
        middle_name = fio[2][0].upper().strip()
        return f"{last_name} {first_name}.{middle_name}."
    elif len(fio) == 2:
        last_name = fio[0].capitalize().strip()
        first_name = fio[1][0].upper().strip()
        return f"{last_name} {first_name}."
    elif len(fio) == 0:
        raise ValueError('Пустое ФИО')


def format_group(group: str) -> str:
    if len(group) >= 1:
        return f"гр. {group}"
    else:
        raise ValueError('Пустая группа')


def format_gpa(gpa: float) -> str:
    if isinstance(gpa, float):
        return f"GPA {gpa:.2f}"
    else:
        raise ValueError('Неверный тип GPA')


def format_record(rec: tuple[str, str, float]) -> str:
    name = format_name(rec[0])
    group = format_group(rec[1])
    gpa = format_gpa(rec[2])
    return f"{name}, {group}, {gpa}"


print(format_record(rec=("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(rec=("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(rec=("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(rec=("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))