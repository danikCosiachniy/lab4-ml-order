from pathlib import Path

import numpy as np
from tensorflow.keras.utils import load_img, img_to_array

from configs.config import IMAGE_SIZE, VAL_DIR, PREDICTIONS_DIR


def predict_image(model, image_path: Path) -> str:
    """
    Делает предсказание для одного изображения.
    Возвращает строку с результатом.
    """
    img = load_img(image_path, target_size=IMAGE_SIZE)
    img = img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    score = float(model.predict(img, verbose=0)[0][0])

    if score < 0.5:
        prediction = "Normal"
    else:
        prediction = "Pneumonia"

    result = (
        f"File: {image_path}\n"
        f"Score: {score:.6f}\n"
        f"Prediction: {prediction}\n"
    )

    return result


def find_sample_images() -> list[Path]:
    """
    Ищет по одному примеру из val/NORMAL и val/PNEUMONIA.
    Если в val мало файлов, можно заменить VAL_DIR на TEST_DIR.
    """
    normal_dir = VAL_DIR / "NORMAL"
    pneumonia_dir = VAL_DIR / "PNEUMONIA"

    normal_images = list(normal_dir.glob("*"))
    pneumonia_images = list(pneumonia_dir.glob("*"))

    sample_images = []

    if normal_images:
        sample_images.append(normal_images[0])

    if pneumonia_images:
        sample_images.append(pneumonia_images[0])

    return sample_images


def predict_samples(model) -> None:
    """
    Проверяет модель на нескольких изображениях из val.
    """
    PREDICTIONS_DIR.mkdir(parents=True, exist_ok=True)

    sample_images = find_sample_images()

    if not sample_images:
        print(
            "\nНе найдены изображения в data/chest_xray/val. "
            "Проверь, скачан ли датасет."
        )
        return

    output_text = []

    print("\nПроверка модели на отдельных изображениях:")

    for image_path in sample_images:
        result = predict_image(model, image_path)
        print(result)
        output_text.append(result)

    prediction_path = PREDICTIONS_DIR / "sample_predictions.txt"

    with open(prediction_path, "w", encoding="utf-8") as file:
        file.write("\n".join(output_text))

    print(f"Предсказания сохранены: {prediction_path}")