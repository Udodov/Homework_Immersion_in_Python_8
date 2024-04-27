import json
import pickle
from pathlib import Path
from typing import Iterator

BASE_DATA_PATH = Path('data_lesson_8')
PICKLE_DIR = BASE_DATA_PATH / 'pickles'
PICKLE_DIR.mkdir(exist_ok=True)


def json_to_pickle(base_path: Path = BASE_DATA_PATH) -> Iterator[Path]:
    for json_file in base_path.glob("*.json"):
        pickle_file = PICKLE_DIR / f"{json_file.stem}.pickle"

        # Загружаем данные из JSON-файла
        json_data = json.loads(json_file.read_bytes())

        # Сериализуем данные в pickle-формат
        pickle_data = pickle.dumps(json_data)

        # Записываем сериализованные данные в pickle-файл
        pickle_file.write_bytes(pickle_data)

        # Возвращаем объект Path для созданного pickle-файла
        yield pickle_file


# Создаем список путей к созданным pickle-файлам
_ = [p for p in json_to_pickle()]
