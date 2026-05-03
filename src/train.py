from configs.config import (
    MODEL_PATH,
    MODELS_DIR,
    EPOCHS,
    STEPS_PER_EPOCH,
    VALIDATION_STEPS,
)
from src.data_loader import create_train_generator, create_test_generator
from src.model import build_classifier
from src.plots import save_training_plots


def train_model():
    """
    Полный цикл обучения:
    1. создание генераторов;
    2. создание CNN;
    3. обучение;
    4. сохранение модели;
    5. сохранение графиков.
    """
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    training_set = create_train_generator()
    test_set = create_test_generator(shuffle=True)

    classifier = build_classifier()

    print("\nСтруктура модели:")
    classifier.summary()

    print("\nНачинается обучение модели...")

    history = classifier.fit(
        training_set,
        steps_per_epoch=STEPS_PER_EPOCH,
        epochs=EPOCHS,
        validation_data=test_set,
        validation_steps=VALIDATION_STEPS,
    )

    classifier.save(MODEL_PATH)
    print(f"\nМодель сохранена: {MODEL_PATH}")

    save_training_plots(history)
    print("Графики обучения сохранены в outputs/plots")

    return classifier, history