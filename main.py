from configs.config import (
    TRAIN_DIR,
    TEST_DIR,
    VAL_DIR,
    OUTPUT_DIR,
    MODELS_DIR,
    PLOTS_DIR,
    PREDICTIONS_DIR,
)
from scripts.download_dataset import download_dataset
from src.train import train_model
from src.evaluate import evaluate_model
from src.predict import predict_samples


def create_output_dirs() -> None:
    """
    Создает папки для результатов работы программы.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    PREDICTIONS_DIR.mkdir(parents=True, exist_ok=True)


def dataset_is_ready() -> bool:
    """
    Проверяет, что структура датасета существует и содержит изображения.

    Просто наличие папок недостаточно.
    У тебя папки уже были, но они могли быть пустыми.
    Поэтому проверяем наличие файлов внутри классов NORMAL и PNEUMONIA.
    """
    required_dirs = [
        TRAIN_DIR / "NORMAL",
        TRAIN_DIR / "PNEUMONIA",
        TEST_DIR / "NORMAL",
        TEST_DIR / "PNEUMONIA",
        VAL_DIR / "NORMAL",
        VAL_DIR / "PNEUMONIA",
    ]

    for directory in required_dirs:
        if not directory.exists():
            print(f"Не найдена папка датасета: {directory}")
            return False

        image_files = (
            list(directory.glob("*.jpeg"))
            + list(directory.glob("*.jpg"))
            + list(directory.glob("*.png"))
        )

        if len(image_files) == 0:
            print(f"Папка датасета пустая: {directory}")
            return False

    return True


def prepare_dataset() -> None:
    """
    Проверяет датасет.
    Если датасет не найден или папки пустые — запускает загрузку.
    """
    if dataset_is_ready():
        print("Датасет найден. Повторная загрузка не требуется.")
        return

    print("Датасет не найден или структура неполная.")
    print("Запускается автоматическая загрузка датасета...")

    download_dataset(force=True)

    if not dataset_is_ready():
        raise RuntimeError(
            "Датасет был скачан, но структура всё равно некорректная. "
            "Проверь папку data/chest_xray вручную."
        )

    print("Датасет успешно подготовлен.")


def main() -> None:
    """
    Главная точка запуска лабораторной работы №4, вариант 12.
    """
    print("Лабораторная работа №4")
    print("Разработка нейронной сети для распознавания пневмонии")
    print("Вариант 12")

    create_output_dirs()
    prepare_dataset()

    model, history = train_model()

    evaluate_model(model)

    predict_samples(model)

    print("\nРабота завершена.")


if __name__ == "__main__":
    main()