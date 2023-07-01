from sys import argv
from argparse import ArgumentParser
import CLAudioConverter


def create_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "-id",
        "--input_dir",
        default="./",
        help='Source files directory | Каталог исходных файлов (default = "./")',
    )
    parser.add_argument(
        "-i",
        "--input",
        nargs="+",
        default=[],
        help="List of input file formats | Список форматов входных файлов"
        + '(for example, "*.mp3" "*.wav") (default = [])',
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file format | Формат выходного файла"
        + '(for example, ".mp3" or ".opus")',
    )
    parser.add_argument(
        "-od",
        "--output_dir",
        default="./",
        help='Output directory | Выходной каталог (default = "./")',
    )
    parser.add_argument(
        "-r",
        "--remove",
        default=False,
        help="Delete original file after conversion | "
        + "Удалить исходный файл после преобразования (defaut = False)",
    )
    parser.add_argument(
        "-fl",
        "--file_list",
        nargs="+",
        default=[],
        help="List of individual files to be converted | "
        + "Список отдельных файлов для преобразования (default = [])",
    )
    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args(argv[1:])

    if len(namespace.file_list) > 0:
        files = CLAudioConverter.check_files(namespace.file_list)
    else:
        files = CLAudioConverter.get_dir_lst(namespace.input_dir, namespace.input)
    print("Current list:")
    for f in files:
        print(f)
    CLAudioConverter.convert(
        files, namespace.output, namespace.output_dir, namespace.remove
    )
    # CLAudioConverter.remove_duplicates(namespace.input_dir, namespace.output_dir, namespace.input)


if __name__ == "__main__":
    main()
