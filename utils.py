import time
from pathlib import Path


def check_staleness(unix_time: int, delta: int) -> bool:
    now = get_unix_time()
    return now - unix_time > delta * 1000  # for milliseconds adjustment


def get_unix_time() -> int:
    return int(time.time()) * 1000


def invert_dict(data: dict) -> dict:
    return {v: k for k, v in data.items()}


def get_root_dir() -> Path:
    return Path(__file__).parent
