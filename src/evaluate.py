import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

from configs.config import PREDICTIONS_DIR
from src.data_loader import create_test_generator


def evaluate_model(model) -> None:
    """
    Оценивает модель на тестовой выборке.
    Дополнительно выводит classification report и confusion matrix.
    """
    PREDICTIONS_DIR.mkdir(parents=True, exist_ok=True)

    test_set = create_test_generator(shuffle=False)

    print("\nОценка модели на тестовой выборке:")
    loss, accuracy = model.evaluate(test_set)
    print(f"Test loss: {loss:.4f}")
    print(f"Test accuracy: {accuracy:.4f}")

    predictions = model.predict(test_set)
    predicted_classes = (predictions >= 0.5).astype(int).reshape(-1)

    true_classes = test_set.classes
    class_labels = list(test_set.class_indices.keys())

    report = classification_report(
        true_classes,
        predicted_classes,
        target_names=class_labels,
    )

    matrix = confusion_matrix(true_classes, predicted_classes)

    print("\nClassification report:")
    print(report)

    print("\nConfusion matrix:")
    print(matrix)

    report_path = PREDICTIONS_DIR / "classification_report.txt"

    with open(report_path, "w", encoding="utf-8") as file:
        file.write("Classification report\n")
        file.write("=====================\n\n")
        file.write(report)
        file.write("\n\nConfusion matrix\n")
        file.write("================\n")
        file.write(np.array2string(matrix))

    print(f"\nОтчет по классификации сохранен: {report_path}")