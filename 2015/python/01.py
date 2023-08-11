import itertools
import pathlib
from collections.abc import Iterator, Callable

brackets_map = {"(": 1, ")": -1}


def map_parens(parentheses: str) -> Iterator[int]:
    return map(lambda c: brackets_map[c], parentheses)


def calculate_floor(
    parentheses: str, map_func: Callable[[str], Iterator[int]] = map_parens
) -> int:
    return sum(map_func(parentheses))


def get_idx_basement(parentheses: str) -> int:
    idx = -1
    acc = itertools.accumulate(map_parens(parentheses))
    for idx, fl in enumerate(acc, start=1):
        if fl == -1:
            break

    return idx


if __name__ == "__main__":
    path = "../inputs/adventofcode.com_2015_day_1_input.txt"

    parens = pathlib.Path(path).read_text()

    # Part 1
    floor = calculate_floor(parens)
    print("Floor:", floor)

    # Part 2
    paren_idx = get_idx_basement(parens)
    print("Index:", paren_idx)
