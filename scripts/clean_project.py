import argparse
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from configs.config import (
    DATA_DIR,
    OUTPUT_DIR,
    MODELS_DIR,
    PLOTS_DIR,
    PREDICTIONS_DIR,
)


def remove_path(path: Path) -> None:
    """
    Удаляет файл или папку, если они существуют.
    """
    if not path.exists():
        print(f"Пропущено, не найдено: {path}")
        return

    if path.is_file():
        path.unlink()
        print(f"Удален файл: {path}")
        return

    shutil.rmtree(path)
    print(f"Удалена папка: {path}")


def recreate_dir(path: Path) -> None:
    """
    Создает пустую папку после удаления.
    """
    path.mkdir(parents=True, exist_ok=True)
    print(f"Создана пустая папка: {path}")


def clean_models() -> None:
    remove_path(MODELS_DIR)
    recreate_dir(MODELS_DIR)


def clean_plots() -> None:
    remove_path(PLOTS_DIR)
    recreate_dir(PLOTS_DIR)


def clean_predictions() -> None:
    remove_path(PREDICTIONS_DIR)
    recreate_dir(PREDICTIONS_DIR)


def clean_outputs() -> None:
    remove_path(OUTPUT_DIR)

    recreate_dir(MODELS_DIR)
    recreate_dir(PLOTS_DIR)
    recreate_dir(PREDICTIONS_DIR)


def clean_dataset() -> None:
    remove_path(DATA_DIR)
    recreate_dir(DATA_DIR)


def clean_all() -> None:
    clean_outputs()
    clean_dataset()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Очистка результатов проекта лабораторной работы №4."
    )

    parser.add_argument(
        "--target",
        choices=[
            "models",
            "plots",
            "predictions",
            "outputs",
            "dataset",
            "all",
        ],
        required=True,
        help="Что нужно очистить.",
    )

    args = parser.parse_args()

    if args.target == "models":
        clean_models()
    elif args.target == "plots":
        clean_plots()
    elif args.target == "predictions":
        clean_predictions()
    elif args.target == "outputs":
        clean_outputs()
    elif args.target == "dataset":
        clean_dataset()
    elif args.target == "all":
        clean_all()


if __name__ == "__main__":
    main()