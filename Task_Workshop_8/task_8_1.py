"""Вспоминаем задачу 3 из прошлого семинара.
Мы сформировали текстовый файл с псевдоименем и произведением чисел.
Напишите функцию, которая создает из созданного ранее файла, новый с данными в формате JSON.
Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки."""

import json
from pathlib import Path
from typing import NoReturn

# Определение базового пути к данным
BASE_DATA_PATH = Path('data_lesson_8')

# Определение пути к файлу с входными данными
FILE_PATH = "E:\\Учеба GB\\Погружение в Python. Часть 1 (семинары)" \
            "\\Урок 7. Файлы и файловая система\\Lesson 7. Files and the file system" \
            "\\Task_Workshop_7\\data_lesson_7\\texts\\result.txt"
# Определение пути к файлу вывода, используя BASE_DATA_PATH
OUTPUT_FILE_PATH = BASE_DATA_PATH / "output.json"


def convert_to_json(input_file_path: str, output_file_path: Path) -> NoReturn:
    """Читает файл, преобразует данные в JSON и сохраняет в новый файл."""
    # Проверка существования директории и создание если необходимо
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(input_file_path, 'r', encoding='utf-8') as file:
        # Создание списка словарей для каждой строки в файле
        data = [{"Имя": line.split()[0].capitalize(), "Произведение": int(line.split()[1])} for line in file]

    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# Вызов функции для преобразования данных и сохранения их в формате JSON
convert_to_json(FILE_PATH, OUTPUT_FILE_PATH)
