import argparse
from pathlib import Path

from polib import POFile

from sanya.parser import (
    filter_all_words,
    get_all_words,
    get_files,
    is_bad_word,
    load_words,
)


def _parse_arguments() -> argparse.Namespace:
    """Parse cli arguments."""
    parser = argparse.ArgumentParser(prog='sanya')
    parser.add_argument('path', nargs='?', default='.')

    return parser.parse_args()


def _main_parser(
    dictionary: set[str],
    po_files: list[POFile],
) -> None:
    for po_file in po_files:
        words = filter_all_words(get_all_words(po_file))
        for word in words:
            if is_bad_word(word, dictionary):
                message = f'found word: {word} in file: {po_file.fpath}'
                print(message)  # noqa: WPS421


def main() -> None:
    """Main func."""
    args = _parse_arguments()

    dictionary = load_words()
    po_files = get_files(Path(args.path))
    _main_parser(dictionary, po_files)
