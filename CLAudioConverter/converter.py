"""! @brief Конвертер."""

import ffmpeg
from os.path import exists, join, isfile
from os import mkdir, remove
from pathlib import Path


def convert(files: list, res: str, out_dir: str, rf: bool = False):
    """! Конвертация файлов.

    @param files    Список путей аудиофайлов.
    @param res      Результирующий формат аудиофайла (например, '.opus').
    @param out_dir  Пуь директории для выходных файлов.
    @param rf       Удалить оригинальный файл после конвертации (если True).
    """

    exc_dict = {}
    if not exists(out_dir):
        mkdir(out_dir)
    for file in files:
        out_file = join(out_dir, Path(file).stem + res)
        if isfile(out_file):
            continue
        try:
            ffmpeg.input(file).output(out_file).run()
            if rf:
                remove(file)
        except Exception as e:
            exc_dict[file] = str(e)
    for file in exc_dict:
        print(f"{file} -> {exc_dict[file]}")
