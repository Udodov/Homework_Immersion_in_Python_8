import csv
import hashlib
import json
from pathlib import Path

BASE_DATA_PATH = Path('data_lesson_8')


def process_csv_to_json(input_csv: Path, output_json: Path) -> None:
    """Читает данные из CSV файла, обрабатывает их и сохраняет в JSON файл."""
    with open(input_csv, 'r', encoding='utf-8') as csv_file:
        # Пропускаем заголовок
        next(csv_file)
        processed_data = [
            {
                "Access Level": row[0],
                "User ID": row[1].zfill(10),  # Дополнение ID незначащими нулями
                "Name": row[2].capitalize(),  # Прописная первая буква имени
                "Hash": hashlib.sha256(f"{row[2]}{row[1]}".encode()).hexdigest()  # Хеш на основе имени и ID
            }
            for row in csv.reader(csv_file)
        ]

    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(processed_data, json_file, indent=4)


# Вызов функции для обработки данных и сохранения в JSON
process_csv_to_json(BASE_DATA_PATH / 'users_data.csv', BASE_DATA_PATH / 'processed_users_data.json')
