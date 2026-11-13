import pytest

from sanya.parser import filter_all_words


@pytest.mark.parametrize(
    ('words', 'expected'),
    [
        pytest.param(
            ['привет', 'мир'],
            ['привет', 'мир'],
            id='all-russian-words-kept',
        ),
        pytest.param(
            ['hello', 'world'],
            [],
            id='all-english-words-filtered',
        ),
        pytest.param(
            ['привет', 'hello', 'мир'],
            ['привет', 'мир'],
            id='mixed-words-only-russian-kept',
        ),
        pytest.param(
            ['Привет', 'МИР'],
            ['Привет', 'МИР'],
            id='uppercase-russian-words-kept',
        ),
        pytest.param(
            ['привет123', 'мир!'],
            [],
            id='words-with-digits-and-punctuation-filtered',
        ),
        pytest.param(
            [],
            [],
            id='empty-list-returns-empty-list',
        ),
        pytest.param(
            [''],
            [],
            id='empty-string-filtered',
        ),
        pytest.param(
            ['ёж', 'ъ'],
            ['ёж', 'ъ'],
            id='russian-alphabet-special-letters-kept',
        ),
    ],
)
def test_filter_all_words(words: list[str], expected: list[str]) -> None:
    assert filter_all_words(words) == expected


def test_filter_all_words_preserves_order() -> None:
    words = ['hello', 'мир', 'world', 'привет']
    assert filter_all_words(words) == ['мир', 'привет']


def test_filter_all_words_returns_list() -> None:
    result = filter_all_words(['привет'])
    assert isinstance(result, list)
