"""Practice 3 for quiz 2."""
__author__ = "730466642"


def short_words(input_words: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list: list[str] = list()
    for words in input_words:
        if len(words) < 5:
            new_list.append(words)
        else:  # word is too long
            print(f"{words} is too long!")
    return new_list