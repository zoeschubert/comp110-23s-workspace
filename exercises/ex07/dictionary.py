"""Dictionary functions for EX07."""
__author__ = "730466642"


def invert(inputdict: dict[str, str]) -> dict[str, str]:
    """Invert the keys with the values."""
    new_dict = []
    idx: int = 0
    for key in inputdict:
        # invert the key with its value
        new_dict[idx] == key
        idx += 1
    if key in inputdict > 1:
        # raise an error if key occurs more than once
        raise KeyError(f"{key} occurs more than once in the dictionary.")
    return new_dict  


def favorite_color(colors: dict[str, str]) -> str:
    """Return the most popular favorite color."""
    count: dict[str, str] = {}
    max: int = 0
    popular: str = ""
    for key in colors:
        if key not in count:
            count[key] = 0
        else:  # increase the count by one
            count[key] += 1
        if count[key] > max:
            max == count[key]
            popular == key
    return popular


def count(inputlist: list[str]) -> dict[str, int]:
    """Return a dict that counts the occurrence of values in list."""
    new_dict: dict[str, int] = []
    idx: int = 0
    for item in inputlist:
        if item in new_dict: 
            new_dict[idx] += 1
        else:  # the item is only seen once
            new_dict[idx] == 1
        idx += 1
    return new_dict