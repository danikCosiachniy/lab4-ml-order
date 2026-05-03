import matplotlib.pyplot as plt

from configs.config import PLOTS_DIR


def save_training_plots(history) -> None:
    """
    Сохраняет графики ошибки и точности обучения.
    """
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    # График функции потерь
    plt.figure(figsize=(8, 5))
    plt.plot(history.history["loss"], label="Ошибка на обучении")
    plt.plot(history.history["val_loss"], label="Ошибка на тесте")
    plt.title("Изменение функции потерь в процессе обучения")
    plt.xlabel("Эпоха")
    plt.ylabel("Ошибка loss")
    plt.legend()
    plt.grid(True)
    plt.savefig(PLOTS_DIR / "loss_plot.png", dpi=300, bbox_inches="tight")
    plt.close()

    # График точности
    plt.figure(figsize=(8, 5))
    plt.plot(history.history["accuracy"], label="Точность на обучении")
    plt.plot(history.history["val_accuracy"], label="Точность на тесте")
    plt.title("Изменение точности модели в процессе обучения")
    plt.xlabel("Эпоха")
    plt.ylabel("Точность accuracy")
    plt.legend()
    plt.grid(True)
    plt.savefig(PLOTS_DIR / "accuracy_plot.png", dpi=300, bbox_inches="tight")
    plt.close()