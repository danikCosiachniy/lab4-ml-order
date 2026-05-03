# Инструкция по запуску лабораторной работы №4 на Windows

## 1. Что делает программа

Эта программа обучает нейронную сеть распознавать пневмонию по рентгеновским снимкам лёгких.

Модель определяет один из двух классов:

- `NORMAL` — снимок без пневмонии;
- `PNEUMONIA` — снимок с пневмонией.

Проект сделан для учебной лабораторной работы. Это не медицинская программа и не инструмент для настоящей диагностики.

---

## 2. Что понадобится

На компьютере должны быть установлены:

1. Python;
2. редактор кода, например Visual Studio Code или PyCharm;
3. библиотеки Python из файла `requirements.txt`.

---

## 3. Установка Python на Windows

### 3.1. Проверка, установлен ли Python

Открой командную строку:

1. нажми `Win + R`;
2. введи `cmd`;
3. нажми `Enter`.

В командной строке введи:

```bat
python --version
```

Если Python установлен, появится примерно такой ответ:

```bat
Python 3.11.9
```

Если появилась ошибка:

```bat
'python' is not recognized as an internal or external command
```

значит Python не установлен или не добавлен в системный путь `PATH`.

### 3.2. Как установить Python

1. Открой сайт Python: https://www.python.org/downloads/
2. Нажми кнопку `Download Python`.
3. Скачай установщик для Windows.
4. Запусти скачанный `.exe` файл.
5. На первом экране установки обязательно поставь галочку:

```text
Add python.exe to PATH
```

Это самый важный пункт. Без этой галочки Windows может не находить команду `python`.

После этого нажми:

```text
Install Now
```

Дождись окончания установки.

### 3.3. Проверка после установки

Закрой командную строку и открой ее заново.

Проверь Python:

```bat
python --version
```

Проверь pip:

```bat
pip --version
```

Если обе команды показывают версии, значит Python установлен правильно.

---

## 4. Установка редактора кода

Можно использовать Visual Studio Code или PyCharm.

### Visual Studio Code

1. Открой сайт: https://code.visualstudio.com/
2. Скачай установщик для Windows.
3. Установи Visual Studio Code.
4. Открой Visual Studio Code.
5. Нажми `File` → `Open Folder...`.
6. Выбери папку проекта.

### PyCharm

1. Открой сайт: https://www.jetbrains.com/pycharm/download/
2. Скачай бесплатную версию `Community Edition`.
3. Установи PyCharm.
4. Открой проект через кнопку `Open`.

Дальше в инструкции используется обычная командная строка Windows `cmd`.

---

## 5. Переход в папку проекта

Допустим, проект находится здесь:

```bat
C:\Users\Student\Desktop\lab4-ml-order
```

В командной строке нужно перейти в эту папку:

```bat
cd C:\Users\Student\Desktop\lab4-ml-order
```

Если проект лежит в другом месте, путь нужно заменить на свой.

Например:

```bat
cd C:\Users\User\Documents\lab4-ml-order
```

Проверить, что открыта правильная папка, можно командой:

```bat
dir
```

В списке должны быть такие файлы и папки:

```text
configs
main.py
requirements.txt
scripts
src
data
outputs
readme.md
```

Если этих файлов нет, значит командная строка открыта не в папке проекта.

---

## 6. Проверка версии Python

В этой инструкции виртуальное окружение не используется. Проект запускается напрямую через установленную версию Python.

Проверь версию Python:

```bat
python --version
```

Рекомендуется использовать Python 3.10 или Python 3.11.

Если на компьютере установлено несколько версий Python, можно проверить их так:

```bat
py -0
```

Команда покажет список доступных версий Python.

Пример:

```text
Installed Pythons found by py Launcher for Windows
 -3.11-64
 -3.10-64
```

Если нужно запускать проект конкретной версией Python, используй команду через `py`.

Например, для Python 3.11:

```bat
py -3.11 main.py
```

А для установки библиотек именно в Python 3.11:

```bat
py -3.11 -m pip install -r requirements.txt
```

---

## 7. Обновление pip

Перед установкой библиотек обнови `pip`:

```bat
python -m pip install --upgrade pip
```

`pip` — это программа для установки библиотек Python.

---

## 8. Установка библиотек проекта

Все нужные библиотеки указаны в файле:

```text
requirements.txt
```

Установи их командой:

```bat
pip install -r requirements.txt
```

Установка может занять несколько минут. Это нормально, потому что библиотека TensorFlow довольно большая.

Если установка завершилась без красных ошибок, можно запускать проект.

---

## 9. Скачивание датасета

Датасет — это набор рентгеновских снимков, на которых обучается модель.

Проект умеет скачивать датасет автоматически. Отдельно можно выполнить:

```bat
python -m scripts\download_dataset.py
```

После скачивания должна появиться структура:

```text
data\chest_xray\train\NORMAL
data\chest_xray\train\PNEUMONIA
data\chest_xray\test\NORMAL
data\chest_xray\test\PNEUMONIA
data\chest_xray\val\NORMAL
data\chest_xray\val\PNEUMONIA
```

Отдельно запускать скачивание необязательно. При запуске `main.py` программа сама проверяет, есть ли датасет. Если датасета нет или папки пустые, она попробует скачать его автоматически.

---

## 10. Запуск лабораторной работы

Главная команда запуска:

```bat
python main.py
```

После запуска программа:

1. проверит папки проекта;
2. проверит наличие датасета;
3. при необходимости скачает датасет;
4. загрузит изображения;
5. создаст нейронную сеть;
6. обучит модель;
7. сохранит обученную модель;
8. построит графики обучения;
9. проверит модель на тестовой выборке;
10. сохранит результаты проверки.

Во время обучения будут появляться строки такого вида:

```text
Epoch 1/10
40/40 [==============================] - loss: 0.6900 - accuracy: 0.6000 - val_loss: 0.6500 - val_accuracy: 0.7000
```

Это нормальный процесс обучения.

---

## 11. Что должно появиться после запуска

После успешного запуска появится папка `outputs` с результатами.

### Модель

```text
outputs\models\pneumonia_cnn_variant12.keras
```

Это сохраненная обученная нейронная сеть.

### Графики

```text
outputs\plots\loss_plot.png
outputs\plots\accuracy_plot.png
```

`loss_plot.png` показывает изменение ошибки модели.

`accuracy_plot.png` показывает изменение точности модели.

### Результаты проверки

```text
outputs\predictions\classification_report.txt
outputs\predictions\sample_predictions.txt
```

`classification_report.txt` содержит общие метрики качества.

`sample_predictions.txt` содержит примеры предсказаний модели.

---

## 12. Как понять, что всё сработало

После завершения в командной строке должно появиться сообщение:

```text
Работа завершена.
```

Также должны существовать файлы:

```text
outputs\models\pneumonia_cnn_variant12.keras
outputs\plots\loss_plot.png
outputs\plots\accuracy_plot.png
outputs\predictions\classification_report.txt
outputs\predictions\sample_predictions.txt
```

Если эти файлы появились, значит модель обучилась и проверка была выполнена.

---

## 13. Как проверить результат модели

### 13.1. Проверка файла с предсказаниями

Открой файл:

```text
outputs\predictions\sample_predictions.txt
```

Внутри будет примерно такой результат:

```text
File: C:\Users\Student\Desktop\lab4-ml-order\data\chest_xray\val\NORMAL\example.jpeg
Score: 0.123456
Prediction: Normal

File: C:\Users\Student\Desktop\lab4-ml-order\data\chest_xray\val\PNEUMONIA\example.jpeg
Score: 0.876543
Prediction: Pneumonia
```

`Prediction` — итоговый ответ модели.

Возможные значения:

- `Normal` — модель считает, что снимок нормальный;
- `Pneumonia` — модель считает, что на снимке пневмония.

`Score` — численный результат модели от 0 до 1.

Правило такое:

- если `Score < 0.5`, программа выводит `Normal`;
- если `Score >= 0.5`, программа выводит `Pneumonia`.

### 13.2. Проверка общего качества

Открой файл:

```text
outputs\predictions\classification_report.txt
```

Там будут метрики:

```text
precision
recall
f1-score
accuracy
```

Самая простая метрика — `accuracy`.

Например:

```text
accuracy 0.82
```

Это означает, что модель правильно классифицировала примерно 82% тестовых изображений.

Но для медицинских данных одной `accuracy` недостаточно. Нужно также смотреть `precision`, `recall` и `f1-score`, потому что модель может хорошо угадывать большинство изображений, но плохо находить один из классов.

---

## 14. Как проверить модель на своем снимке

В базовой версии проекта проверка отдельных изображений выполняется на примерах из папки `val`.

Чтобы проверить свое изображение, можно положить его в одну из папок:

```text
data\chest_xray\val\NORMAL
```

или:

```text
data\chest_xray\val\PNEUMONIA
```

После этого снова запустить:

```bat
python main.py
```

Программа обучит модель и сделает предсказания для изображений из `val`.

Минус этого способа: модель обучается заново.

Более правильный вариант — добавить отдельный скрипт `predict_one.py`, который будет проверять один снимок без повторного обучения.

Пример желаемой команды:

```bat
python scripts\predict_one.py --image C:\Users\Student\Desktop\test_xray.jpeg
```

Если такого файла нет, значит проверка одного изображения без переобучения в проект еще не добавлена.

---

## 15. Очистка результатов

В проекте есть скрипт очистки.

Очистить только модели:

```bat
python scripts\clean_project.py --target models
```

Очистить только графики:

```bat
python scripts\clean_project.py --target plots
```

Очистить только предсказания:

```bat
python scripts\clean_project.py --target predictions
```

Очистить все результаты, но оставить датасет:

```bat
python scripts\clean_project.py --target outputs
```

Очистить только датасет:

```bat
python scripts\clean_project.py --target dataset
```

Очистить вообще всё:

```bat
python scripts\clean_project.py --target all
```

После очистки проект можно снова запустить:

```bat
python main.py
```

Если датасет был удален, программа скачает его заново.

---

## 16. Частые ошибки

### Ошибка: `'python' is not recognized as an internal or external command`

Причина: Python не установлен или не добавлен в `PATH`.

Решение:

1. переустановить Python;
2. при установке поставить галочку `Add python.exe to PATH`;
3. закрыть командную строку;
4. открыть командную строку заново;
5. проверить:

```bat
python --version
```

### Ошибка: `ModuleNotFoundError: No module named 'configs'`

Причина: команда запущена не из корня проекта.

Решение:

```bat
cd C:\Users\Student\Desktop\lab4-ml-order
python main.py
```

Путь нужно заменить на тот, где реально лежит проект.

### Ошибка: `No module named tensorflow`

Причина: библиотеки не установлены в ту версию Python, которой запускается проект.

Решение:

```bat
python -m pip install -r requirements.txt
```

Если используется конкретная версия Python, например 3.11, выполни:

```bat
py -3.11 -m pip install -r requirements.txt
py -3.11 main.py
```

### Ошибка: `No such file or directory`

Причина: указан неправильный путь или командная строка открыта не в папке проекта.

Решение:

```bat
cd C:\Users\Student\Desktop\lab4-ml-order
```

Потом повторить нужную команду.

### Ошибка при скачивании датасета

Возможные причины:

1. нет интернета;
2. Kaggle временно недоступен;
3. не установилась библиотека `kagglehub`;
4. изменилась структура датасета.

Решение:

```bat
pip install --upgrade kagglehub
python scripts\download_dataset.py
```

Если автоматическая загрузка не работает, датасет можно скачать вручную и разложить по папкам:

```text
data\chest_xray\train\NORMAL
data\chest_xray\train\PNEUMONIA
data\chest_xray\test\NORMAL
data\chest_xray\test\PNEUMONIA
data\chest_xray\val\NORMAL
data\chest_xray\val\PNEUMONIA
```

---

## 17. Полный запуск с нуля

Если Python уже установлен и проект находится на рабочем столе, можно выполнить команды по порядку:

```bat
cd C:\Users\Student\Desktop\lab4-ml-order
python --version
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

После завершения нужно проверить папки:

```text
outputs\models
outputs\plots
outputs\predictions
```

---

## 18. Что вставить в отчет

В отчет можно добавить:

1. цель работы;
2. описание структуры проекта;
3. описание используемого датасета;
4. листинг основных файлов программы;
5. график `loss_plot.png`;
6. график `accuracy_plot.png`;
7. результаты из `classification_report.txt`;
8. примеры предсказаний из `sample_predictions.txt`;
9. вывод.

---

## 19. Краткий вывод

В ходе лабораторной работы была разработана сверточная нейронная сеть для бинарной классификации рентгеновских снимков лёгких. Модель определяет один из двух классов: `NORMAL` или `PNEUMONIA`.

Для обучения использовался датасет с заранее разделенными папками `train`, `test` и `val`. В проекте реализованы отдельные модули для загрузки данных, создания модели, обучения, оценки качества, построения графиков и проверки изображений.

После обучения модель сохраняется в файл, а результаты проверки записываются в папку `outputs`. Полученные графики позволяют оценить изменение ошибки и точности модели, а файл `classification_report.txt` показывает качество классификации на тестовой выборке.