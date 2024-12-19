from functools import cache
from pathlib import Path

"""
Idea Part 1:
Idea 1:
Match the first part of the desired pattern with the available patterns.
Greedy, first match is taken, leads to errors when the first match is only a part of another pattern, that would actually lead to the correct match.
So: NOT POSSIBLE!
Idea 2:
Start with the longest availabe pattern has the same error!
Idea 3:
Try every string with the removed pattern if the string begins with the pattern.
Recursively count how many possiblities there are.
ONLY POSSIBLE WITH CACHING!!!
"""


def algorithm_1(input_filename: str) -> int:
    @cache
    def count(wanted: str):
        possibilities = sum(
            count(wanted.removeprefix(p))
            for p in available_patterns
            if wanted.startswith(p)
        )
        return possibilities or wanted == ""

    path = Path(input_filename)
    with open(path, "r") as file:
        available_patterns = [pattern for pattern in next(file)[:-1].split(", ")]
        next(file)
        possible_patterns = 0
        for line in file:
            desired_pattern = line[:-1]
            possible = count(desired_pattern)
            if possible != False:
                possible_patterns += 1
        return possible_patterns


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    @cache
    def count(wanted: str):
        possibilities = sum(
            count(wanted.removeprefix(p))
            for p in available_patterns
            if wanted.startswith(p)
        )
        return possibilities or wanted == ""

    path = Path(input_filename)
    with open(path, "r") as file:
        available_patterns = [pattern for pattern in next(file)[:-1].split(", ")]
        next(file)
        possible_combinations = 0
        for line in file:
            desired_pattern = line[:-1]
            possible = count(desired_pattern)
            if possible != False:
                possible_combinations += possible
        return possible_combinations


# Helping functions


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 6
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 16
    algorithm_answer = algorithm_2(filename)
    return expected_answer == algorithm_answer


def solve_part1() -> int:
    filename = "./input_files/puzzle.txt"
    algorithm_answer = algorithm_1(filename)
    return algorithm_answer


def solve_part2() -> int:
    filename = "./input_files/puzzle.txt"
    algorithm_answer = algorithm_2(filename)
    return algorithm_answer


if __name__ == "__main__":
    if test_part1():
        answer = solve_part1()
        print(f"Todays answer of part 1 is {answer}")
    else:
        print("Test of part 1 was not successfull")

    if test_part2():
        answer = solve_part2()
        print(f"Todays answer of part 2 is {answer}")
    else:
        print("Test of part 2 was not successfull")
