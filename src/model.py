from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

from configs.config import INPUT_SHAPE


def build_classifier() -> Sequential:
    """
    Создает сверточную нейронную сеть для бинарной классификации:
    NORMAL / PNEUMONIA.

    Архитектура соответствует логике из методички:
    Conv2D -> MaxPooling2D -> Conv2D -> MaxPooling2D -> Flatten -> Dense -> Dense.
    """
    classifier = Sequential(name="pneumonia_cnn_variant12")

    classifier.add(
        Conv2D(
            filters=64,
            kernel_size=(3, 3),
            input_shape=INPUT_SHAPE,
            activation="relu",
        )
    )
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    classifier.add(
        Conv2D(
            filters=32,
            kernel_size=(3, 3),
            activation="relu",
        )
    )
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    classifier.add(Flatten())

    classifier.add(Dense(units=104, activation="relu"))

    classifier.add(Dense(units=1, activation="sigmoid"))

    classifier.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    return classifier