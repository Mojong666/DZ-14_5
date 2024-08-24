import json


def employees_rewrite(sort_type):
    # Приводим ключ сортировки к нижнему регистру
    sort_key = sort_type.lower()

    # Открываем файл employees.json и загружаем данные
    with open('employees.json', 'r') as file:
        data = json.load(file)

    employees = data.get("employees", [])

    # Проверка наличия ключа в данных сотрудников
    if not employees or sort_key not in {k.lower() for k in employees[0].keys()}:
        raise ValueError('Bad key for sorting')

    # Замена None на пустую строку или 0 для сортировки
    for emp in employees:
        value = emp.get(sort_key)
        if value is None:
            if isinstance(value, str) or isinstance(value, type(None)):
                emp[sort_key] = ""
            elif isinstance(value, (int, float)):
                emp[sort_key] = 0
            else:
                raise ValueError(f"Unsupported data type: {type(value)} for key: {sort_key}")

    # Примерное значение для определения типа данных
    sample_value = employees[0].get(sort_key)

    # Сортировка в зависимости от типа данных
    if isinstance(sample_value, str):
        sorted_employees = sorted(employees, key=lambda x: x.get(sort_key).lower())
    elif isinstance(sample_value, (int, float)):
        sorted_employees = sorted(employees, key=lambda x: x.get(sort_key), reverse=True)
    else:
        raise ValueError(f"Unsupported data type: {type(sample_value)} for key: {sort_key}")

    # Создаем структуру для записи в JSON
    sorted_data = {"employees": sorted_employees}

    # Формируем имя выходного файла
    output_filename = f'employees_{sort_key}_sorted.json'

    # Записываем отсортированные данные в новый JSON файл
    with open(output_filename, 'w') as file:
        json.dump(sorted_data, file, indent=4)

    print(f'Data sorted by {sort_type} and saved to {output_filename}')


# Примеры использования:
# employees_rewrite('lastname')  # Сортировка по фамилии
# employees_rewrite('department')  # Сортировка по отделу
# employees_rewrite('salary')  # Сортировка по зарплате
employees_rewrite('firstname')  # Сортировка по имени
