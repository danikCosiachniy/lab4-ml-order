from pathlib import Path


# Корневая папка проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Папки с данными
DATA_DIR = BASE_DIR / "data" / "chest_xray"
TRAIN_DIR = DATA_DIR / "train"
TEST_DIR = DATA_DIR / "test"
VAL_DIR = DATA_DIR / "val"

# Папки результатов
OUTPUT_DIR = BASE_DIR / "outputs"
MODELS_DIR = OUTPUT_DIR / "models"
PLOTS_DIR = OUTPUT_DIR / "plots"
PREDICTIONS_DIR = OUTPUT_DIR / "predictions"

# Параметры изображения из методички
IMAGE_SIZE = (64, 64)
COLOR_MODE = "rgb"
INPUT_SHAPE = (64, 64, 3)

# Параметры обучения из методички
BATCH_SIZE = 4
EPOCHS = 10
STEPS_PER_EPOCH = 40
VALIDATION_STEPS = 8

# Вариант работы
VARIANT = 12

# Сохранение модели
MODEL_NAME = "pneumonia_cnn_variant12.keras"
MODEL_PATH = MODELS_DIR / MODEL_NAME

# Датасет Kaggle
# Альтернатива: "paultimothymooney/chest-xray-pneumonia"
KAGGLE_DATASET = "paultimothymooney/chest-xray-pneumonia"