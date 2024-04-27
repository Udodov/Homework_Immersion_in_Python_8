"""Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа.
После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа.
Идентификатор группируется по уровню доступа. Идентификатор пользователя выступает ключом по имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться."""

import json
from pathlib import Path

# Константы для минимального и максимального уровня доступа
MIN_ACCESS_LEVEL = 1
MAX_ACCESS_LEVEL = 9

# Базовый путь к директории с данными
BASE_DATA_PATH = Path('data_lesson_8')
# Убедимся, что директория существует
BASE_DATA_PATH.mkdir(parents=True, exist_ok=True)


def load_data(data_file_path: Path) -> dict:
    """Загружает данные из JSON файла."""
    if not data_file_path.exists():
        return {}  # Возвращаем пустой словарь, если файл не существует
    with open(data_file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_data(data_file_path: Path, data: dict) -> None:
    """Сохраняет данные в JSON файл."""
    with open(data_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_user(data_file_path: Path) -> None:
    """Добавляет пользователя в JSON файл с группировкой по уровню доступа."""
    data = load_data(data_file_path)

    while True:
        name = input("Введите имя (или 'exit' для выхода): ").strip()
        if name.lower() == 'exit':
            print("Выход из программы.")
            break
        if not name:
            print("Имя не может быть пустым.")
            continue

        user_id_input = input("Введите личный идентификатор (или 'exit' для выхода): ").strip()
        if user_id_input.lower() == 'exit':
            print("Выход из программы.")
            break
        if not user_id_input.isdigit():
            print("Идентификатор должен быть числом.")
            continue
        user_id = int(user_id_input)

        access_level_input = input(
            f"Введите уровень доступа от {MIN_ACCESS_LEVEL} до {MAX_ACCESS_LEVEL} (или 'exit' для выхода): ").strip()
        if access_level_input.lower() == 'exit':
            print("Выход из программы.")
            break
        if not access_level_input.isdigit() or not MIN_ACCESS_LEVEL <= int(access_level_input) <= MAX_ACCESS_LEVEL:
            print(f"Уровень доступа должен быть числом от {MIN_ACCESS_LEVEL} до {MAX_ACCESS_LEVEL}.")
            continue
        access_level = str(int(access_level_input))  # Преобразуем в строку для использования в качестве ключа

        # Проверка уникальности идентификатора
        if any(str(user_id) in users for users in data.values()):
            print("Ошибка: Идентификатор должен быть уникальным.")
            continue

        if access_level not in data:
            data[access_level] = {}
        data[access_level][str(user_id)] = name

        save_data(data_file_path, data)
        print("Пользователь добавлен.")


# Определение пути к файлу данных
data_file = BASE_DATA_PATH / "users_data.json"
add_user(data_file)
