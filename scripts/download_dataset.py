import shutil
import sys
from pathlib import Path

import kagglehub

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from configs.config import DATA_DIR, KAGGLE_DATASET


def find_chest_xray_dir(download_path: Path) -> Path:
    """
    Ищет папку chest_xray внутри скачанного Kaggle dataset.
    У разных версий датасета структура может отличаться.
    """
    candidates = list(download_path.rglob("chest_xray"))

    if not candidates:
        raise FileNotFoundError(
            "Не найдена папка chest_xray внутри скачанного датасета. "
            "Проверь структуру скачанного архива."
        )

    return candidates[0]


def copy_dataset(source_dir: Path, target_dir: Path) -> None:
    """
    Копирует датасет в папку проекта data/chest_xray.
    Если папка уже существует, она удаляется и создается заново.
    """
    if target_dir.exists():
        shutil.rmtree(target_dir)

    shutil.copytree(source_dir, target_dir)


def download_dataset(force: bool = False) -> None:
    """
    Скачивает датасет и копирует его в data/chest_xray.

    force=False:
        если датасет уже есть, повторно не скачивает.

    force=True:
        удаляет старый датасет и скачивает заново.
    """
    if DATA_DIR.exists() and not force:
        print(f"Датасет уже найден: {DATA_DIR}")
        return

    print("Скачивание датасета Kaggle...")
    download_path = Path(kagglehub.dataset_download(KAGGLE_DATASET))

    print(f"Датасет скачан в: {download_path}")

    chest_xray_source = find_chest_xray_dir(download_path)

    print(f"Найдена папка chest_xray: {chest_xray_source}")
    print(f"Копирование в проект: {DATA_DIR}")

    copy_dataset(chest_xray_source, DATA_DIR)

    print("Датасет готов.")
    print(DATA_DIR / "train")
    print(DATA_DIR / "test")
    print(DATA_DIR / "val")


def main() -> None:
    download_dataset(force=True)


if __name__ == "__main__":
    main()