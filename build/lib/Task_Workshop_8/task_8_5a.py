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
        pickle_file.write_bytes(pickle.dumps(json.loads(json_file.read_bytes())))
        yield pickle_file


_ = [p for p in json_to_pickle()]
