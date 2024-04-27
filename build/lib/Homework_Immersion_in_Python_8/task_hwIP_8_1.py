import csv
import json
import pickle
from pathlib import Path
from typing import Union

# Базовый путь к директории с данными.
BASE_DATA_PATH: Path = Path('data_homework_lesson_8')

# Путь к файлу результатов в формате JSON.
RESULT_JSON: Path = BASE_DATA_PATH / 'result.json'

# Путь к файлу результатов в формате CSV.
RESULT_CSV: Path = BASE_DATA_PATH / 'result.csv'

# Путь к файлу результатов в формате pickle.
RESULT_PICKLE: Path = BASE_DATA_PATH / 'result.pickle'

# Объединенный тип данных для пути к файлу или директории и их размера.
FileSystemObject = Union[Path, int]


def get_dir_size(path: Path) -> int:
    """
    Рекурсивно вычисляет общий размер директории.

    Args: path (Path): Путь к директории.
    Returns: int: Общий размер директории в байтах.
    """
    total_size: int = 0
    for entry in path.iterdir():
        if entry.is_file():
            total_size += entry.stat().st_size
        elif entry.is_dir():
            total_size += get_dir_size(entry)
    return total_size


def traverse_directory(directory: Path) -> list[tuple[Path, int]]:
    """
    Рекурсивно обходит директорию и собирает пути и размеры файлов и директорий.

    Args: directory (Path): Путь к директории.
    Returns: list[tuple[Path, int]]: Список кортежей (путь, размер) для файлов и директорий.
    """
    result: list[tuple[Path, int]] = []
    for entry in directory.iterdir():
        if entry.is_file():
            result.append((entry, entry.stat().st_size))
        elif entry.is_dir():
            dir_size = get_dir_size(entry)
            result.append((entry, dir_size))
            result.extend(traverse_directory(entry))
    return result


def save_results(results: list[tuple[Path, int]]) -> None:
    """
    Сохраняет результаты в файлы в форматах JSON, CSV и pickle.

    Args: results (list[tuple[Path, int]]): Список кортежей (путь, размер) для файлов и директорий.
    """
    BASE_DATA_PATH.mkdir(parents=True, exist_ok=True)

    with RESULT_JSON.open('w', encoding='utf-8') as json_file:
        json_data = [(str(path), size) for path, size in results]
        json.dump(json_data, json_file, indent=4)

    with RESULT_CSV.open('w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows((str(path), size) for path, size in results)

    with RESULT_PICKLE.open('wb') as pickle_file:
        pickle.dump(results, pickle_file)


def main() -> None:
    """
    Главная функция программы.
    """
    target_directory: Path = Path(
        'E:\\Учеба GB\\Погружение в Python. Часть 1 (семинары)\\Урок 8. Сериализация\\Lesson 8. Serialization')
    results = traverse_directory(target_directory)
    save_results(results)


if __name__ == '__main__':
    main()