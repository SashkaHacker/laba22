#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Разработайте аналог утилиты tree в Linux. Используйте возможности модуля argparse для
# управления отображением дерева каталогов файловой системы. Добавьте дополнительные
# уникальные возможности в данный программный продукт.


import argparse
from pathlib import Path


def tree(directory, level, max_items):
    def print_tree(folder, prefix="", level=-1):
        if level == 0:
            return
        if folder.is_dir():
            print(prefix + folder.name)
            prefix += "    "
            for idx, path in enumerate(folder.iterdir()):
                if idx == max_items:
                    break
                connector = (
                    "├── " if idx < len(list(folder.iterdir())) - 1 else "└── "
                )
                print_tree(path, prefix + connector, level - 1)

    print_tree(Path(directory), level=level)


def main():
    parser = argparse.ArgumentParser(
        description="Отображение структуры каталогов файловой системы"
    )
    parser.add_argument(
        "directory", nargs="?", default=".", help="Каталог для отображения"
    )
    parser.add_argument(
        "-l",
        "--level",
        type=int,
        default=-1,
        help="Уровень вложенности для отображения",
    )
    parser.add_argument(
        "--length",
        type=int,
        default=1000,
        help="Ограничение на количество отображаемых элементов",
    )
    args = parser.parse_args()
    tree(args.directory, args.level, args.length)


if __name__ == "__main__":
    main()
