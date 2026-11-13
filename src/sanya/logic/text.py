from sanya.constant import RUSSIAN_ALPHABET


def remove_suffix_bad_chars(word: str) -> str:
    """Remove suffix with bad chars."""
    clean_word = list(word)
    while clean_word and not clean_word[-1].isalpha():
        clean_word.pop()

    return ''.join(clean_word)


def is_russian_word(word: str) -> bool:
    """Check that word is russian."""
    return bool(word) and all(
        letter in RUSSIAN_ALPHABET for letter in word.lower()
    )
