from pathlib import Path
from typing import Final

import polib

from sanya.logic.files import iter_po_files
from sanya.logic.text import is_russian_word

_DICTIONARY_PATH: Final = Path(__file__).parent / 'data/dictionary_ru.txt'


def load_words() -> set[str]:
    """Load dictionary from `dictionary_ru.txt`."""
    dictionary: set[str] = set()
    with Path(_DICTIONARY_PATH).open(encoding='utf-8') as words:
        dictionary.update(line.strip() for line in words)
    return dictionary


def filter_all_words(words: list[str]) -> list[str]:
    """Filter and find all russian words."""
    return [word for word in words if is_russian_word(word)]


def get_all_words(po_file: polib.POFile) -> list[str]:
    """Get all words in `.po` file."""
    words = []
    for entry in po_file:
        for word in entry.msgstr.split():
            if '-' in word:
                words.extend(word.split('-'))
            else:
                words.append(word)
    return words


def is_bad_word(word: str, dictionary: set[str]) -> bool:
    """Check that word is bad."""
    return word in dictionary


def get_files(path: Path) -> list[polib.POFile]:
    """Accumulate and get all find files into directory."""
    return [polib.pofile(str(file_path)) for file_path in iter_po_files(path)]
