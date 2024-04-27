"""Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестирования, возьмите pickle версию файла из задачи 4 семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла."""

import csv
import pickle
from pathlib import Path
from typing import Dict, List

BASE_DATA_PATH = Path('data_lesson_8')
PICKLE_FILE = BASE_DATA_PATH / 'pickles' / 'processed_users_data.pickle'
CSV_FILE = BASE_DATA_PATH / 'processed_users_data.csv'


def pickle_to_csv(pickle_file: Path, csv_file: Path) -> None:
    """
    Преобразует pickle файл, содержащий список словарей, в табличный CSV файл.

    Args:
        pickle_file (Path): Путь к pickle файлу.
        csv_file (Path): Путь к CSV файлу для сохранения.
    """
    with open(pickle_file, 'rb') as pickle_f, open(csv_file, 'w', newline='', encoding='utf-8') as csv_f:
        data: List[Dict[str, str]] = pickle.load(pickle_f)
        fieldnames = list(data[0].keys())  # Извлекаем ключи из первого словаря для заголовков столбцов
        writer = csv.DictWriter(csv_f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


# Вызов функции для преобразования pickle файла в CSV
pickle_to_csv(PICKLE_FILE, CSV_FILE)
