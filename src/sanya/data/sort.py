from pathlib import Path
from typing import Final

from sanya.constant import RUSSIAN_ALPHABET

_DICTIONARY_PATH: Final = Path(__file__).parent / 'dictionary_ru.txt'

type WordsByLetter = dict[str, list[str]]


def _create_alphabet() -> WordsByLetter:
    return {letter: [] for letter in RUSSIAN_ALPHABET}


def _fill_alphabet_with_words(words_by_letter: WordsByLetter) -> WordsByLetter:
    with Path(_DICTIONARY_PATH).open(encoding='utf-8') as wrong_words:
        for word in wrong_words:
            clean_word = word.strip('\n')
            first_letter = clean_word[0]
            words_by_letter[first_letter].append(clean_word)
    return words_by_letter


def _sort_words(words_by_letter: WordsByLetter) -> WordsByLetter:
    sorted_alphabet_words = {}

    for letter, words in words_by_letter.items():
        sorted_alphabet_words[letter] = sorted(words)

    return sorted_alphabet_words


def _rewrite_words(words_by_letter: WordsByLetter) -> None:
    with Path(_DICTIONARY_PATH).open('w', encoding='utf-8') as clean_file:
        clean_file.writelines(
            f'{word}\n' for words in words_by_letter.values() for word in words
        )


def _main() -> None:
    _rewrite_words(_sort_words(_fill_alphabet_with_words(_create_alphabet())))


if __name__ == '__main__':
    _main()
