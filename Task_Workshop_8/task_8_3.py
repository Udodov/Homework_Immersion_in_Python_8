"""Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV"""

from pathlib import Path
import csv
import json

BASE_DATA_PATH = Path('data_lesson_8')
JSON_FILE_NAME = 'users_data.json'
CSV_FILE_NAME = 'users_data.csv'


def save_json_to_csv(json_path: Path, csv_path: Path) -> None:
    """Читает данные из JSON файла и сохраняет их в CSV файл."""
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Access Level', 'User ID', 'Name'])  # Заголовки столбцов

        for access_level, users in data.items():
            for user_id, name in users.items():
                csv_writer.writerow([access_level, user_id, name])


# Вызов функции для сохранения данных из JSON в CSV
save_json_to_csv(BASE_DATA_PATH / JSON_FILE_NAME, BASE_DATA_PATH / CSV_FILE_NAME)
