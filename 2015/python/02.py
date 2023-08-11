import heapq
import itertools
import operator
import pathlib


def calculate_paper_surface(length: int, width: int, height: int) -> int:
    dims_products = tuple(
        itertools.starmap(
            operator.mul, itertools.combinations((length, width, height), 2)
        )
    )
    return 2 * sum(dims_products) + min(dims_products)


def calculate_ribbon_length(length: int, width: int, height: int) -> int:
    smallest_sides = heapq.nsmallest(2, (length, width, height))
    return sum(map(lambda x: x * 2, smallest_sides)) + length * width * height


if __name__ == "__main__":
    path = "../inputs/adventofcode.com_2015_day_2_input.txt"

    dims_boxes: tuple[tuple[int, ...], ...] = tuple(
        tuple(map(int, d.split("x")))
        for d in pathlib.Path(path).read_text().split("\n")[:-1]
    )

    # Part 1
    print(
        "Total wrapping paper area:",
        sum(itertools.starmap(calculate_paper_surface, dims_boxes)),
    )

    # Part 2
    print(
        "Total ribbon length:",
        sum(itertools.starmap(calculate_ribbon_length, dims_boxes)),
    )
