"""! @brief Получение списка файлов."""

from os import walk, remove
from os.path import join, isfile
import re
import fnmatch
from pathlib import Path


def make_filter(filter: list):
    """! Создание регулярного выражения для фильтра

    @param filter   Список форматов (['*.mp3', '*.opus'])
    """
    return r"|".join([fnmatch.translate(x) for x in filter])


def check_files(files: list):
    """! Проверка списка файлов на существование.

    @param files    Список путей файлов.

    @return Исходный список с удаленными
    значениями путей несуществующих файлов.
    """
    filenames = [f for f in files if isfile(f)]
    return filenames


def get_dir_lst(path: str, filter: list):
    """! Получение списка файлов из директории с заданным типом.
    Тип определяется по расширению файла.

    @param path      Путь к директории.
    @param filter   Список расширений (фильтр).

    @return Список файлов в директории, соответствующих заданному типу.
    """

    filter = make_filter(filter)
    filenames = next(walk(path), (None, None, []))[2]
    filenames = [f for f in filenames if re.match(filter, f)]
    filenames = [join(path, f) for f in filenames]
    filenames = check_files(filenames)
    return filenames


def remove_duplicates(dir1: str, dir2: str, filter: list):
    """! Удаление дубликатов файлов.
    Файлы, присутствующие в каталоге 1 будут удалены, если они были включены в каталог 2.

    @param path      Путь к директории.
    @param filter   Список расширений (фильтр).

    @return Список файлов в директории, соответствующих заданному типу.
    """

    files1 = get_dir_lst(dir1, filter)
    files2 = get_dir_lst(dir2, filter)
    stems1 = [Path(f).stem for f in files1]
    stems2 = [Path(f).stem for f in files2]
    for i in range(len(files1)):
        if stems1[i] in stems2:
            remove(files1[i])
            i -= 1
