"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle."""

import csv
import pickle
from pathlib import Path
from typing import Dict, List

BASE_DATA_PATH = Path('data_lesson_8')
CSV_FILE = BASE_DATA_PATH / 'processed_users_data.csv'
PICKLE_FILE = BASE_DATA_PATH / 'processed_users_data.pickle'


def csv_to_pickle(csv_file: Path, pickle_file: Path) -> None:
    """
    Читает CSV файл и сохраняет его содержимое в pickle файл.

    Args:
        csv_file (Path): Путь к CSV файлу.
        pickle_file (Path): Путь к pickle файлу для сохранения.
    """
    data: List[Dict[str, str]] = []
    with open(csv_file, 'r', encoding='utf-8') as csv_f:
        reader = csv.reader(csv_f)
        fieldnames = next(reader)  # Извлекаем заголовки столбцов из первой строки
        for row in reader:
            data.append(dict(zip(fieldnames, row)))  # Создаем словарь из заголовков и значений строки

    with open(pickle_file, 'wb') as pickle_f:
        pickle.dump(data, pickle_f)


# Вызов функции для преобразования CSV файла в pickle
csv_to_pickle(CSV_FILE, PICKLE_FILE)
