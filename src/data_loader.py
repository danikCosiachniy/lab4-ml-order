from tensorflow.keras.preprocessing.image import ImageDataGenerator

from configs.config import (
    TRAIN_DIR,
    TEST_DIR,
    VAL_DIR,
    IMAGE_SIZE,
    BATCH_SIZE,
)


def create_train_generator():
    """
    Генератор тренировочных изображений.

    Используется аугментация, как в методичке:
    - нормализация пикселей;
    - сдвиг/искажение;
    - масштабирование;
    - горизонтальное отражение.
    """
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        shear_range=0.4,
        zoom_range=0.3,
        horizontal_flip=True,
    )

    training_set = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="binary",
    )

    return training_set


def create_test_generator(shuffle: bool = False):
    """
    Генератор тестовых изображений.

    shuffle=False нужен для корректного построения confusion matrix,
    чтобы порядок предсказаний совпадал с порядком меток.
    """
    test_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

    test_set = test_datagen.flow_from_directory(
        TEST_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="binary",
        shuffle=shuffle,
    )

    return test_set


def create_val_generator(shuffle: bool = False):
    """
    Генератор проверочных изображений из папки val.
    """
    val_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

    val_set = val_datagen.flow_from_directory(
        VAL_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="binary",
        shuffle=shuffle,
    )

    return val_set