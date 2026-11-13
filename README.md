# sanya

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

`sanya` is a small command-line linter for gettext `.po` translation files.

It scans translated strings (`msgstr`) for Russian words and checks each word
against a built-in dictionary of known misspellings and typos
(`src/sanya/data/dictionary_ru.txt`). Every match is reported together with the
file it was found in, which helps catch spelling mistakes in Russian
translations before they reach production.

The tool accepts a file or a directory as its path argument. Directories are
scanned recursively for `*.po` files; non-Russian words, numbers and
punctuation are ignored.
