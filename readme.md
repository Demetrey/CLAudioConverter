# CLAudioConverter
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Простой конвертер аудио. Использует [FFmpeg](https://ffmpeg.org/) и поддерживает конвертацию соответствующих форматов.
Поддерживает конвертацию списка отдельных файлов и всех файлов каталога с указанным типом (расширением) (см. [Использование](#использование)).

Конвертация выполняется с сохранением тегов исходных файлов (если это возможно).

## Зависимости
 - [FFmpeg](https://ffmpeg.org/) (путь должен быть указан в переменной окружения PATH)
 - [ffmpeg-python (0.2.0)](https://github.com/kkroening/ffmpeg-python)

Для установки зависимостей (кроме FFmpeg):

    pip install requirements.txt

## Использование
Реализация выполнена с использованием Python3.


    usage: python3 ./main.py [-h] [-id INPUT_DIR] [-i INPUT [INPUT ...]] [-o OUTPUT] [-od OUTPUT_DIR] [-r REMOVE] [-fl FILE_LIST [FILE_LIST ...]]

    optional arguments:
    -h, --help            show this help message and exit
    -id INPUT_DIR, --input_dir INPUT_DIR
                            Source files directory | Каталог исходных файлов (default = "./")
    -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                            List of input file formats | Список форматов входных файлов(for example, "*.mp3" "*.wav") (default = [])
    -o OUTPUT, --output OUTPUT
                            Output file format | Формат выходного файла (for example, ".mp3" or ".opus")
    -od OUTPUT_DIR, --output_dir OUTPUT_DIR
                            Output directory | Выходной каталог (default = "./")
    -r REMOVE, --remove REMOVE
                            Delete original file after conversion | Удалить исходный файл после преобразования (defaut = False)
    -fl FILE_LIST [FILE_LIST ...], --file_list FILE_LIST [FILE_LIST ...]
                            List of individual files to be converted | Список отдельных файлов для преобразования (default = [])


В случае, если параметр ```REMOVE``` указан как ```True```, удаление исходных файлов будет выполняться только в случае отсутствия возникновения исключений в ходе конвертации. После окончания конвертации вне зависимости от значения флага ```REMOVE```, будет выведен список исключений вида:

    [FILE_NAME] -> [EXCEPTION TEXT]

Это позволит определить файлы, для которых конвертация не была выполнена или выполнена с ошибками.

## Примеры использования

### Пример 1
Конвертация всех MP3- и AAC-файлов в каталоге ```catalog1``` в OPUS, результат конвертации должен быть помещен в каталог ```catalog2```, файлы, для которых конвертация выполнена без ошибок, должны быть удалены. В случае, если выходной каталог отсутствует, он будет создан.

    python3 ./main.py -id ./catalog1 -i *.mp3 *.aac -o .opus -od ./catalog2 -r True

### Пример 2
Конвертация всех указанных файлов в MP3, результат конвертации должен быть помещен в каталог ```catalog2```, файлы, для которых конвертация выполнена без ошибок должны быть удалены.

    python3 ./main.py -fl ./catalog1/file1.opus ./catalog1/file2.wav -o .mp3 -od ./catalog2 -r True
