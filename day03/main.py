from pathlib import Path
import re


"""
Idea Part 1:
Search the file with Regex to get all mul(X,Y) operations.
"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as f:
        total_sum = 0
        for line in f:
            pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
            all_matches = re.findall(pattern, line)
            product = sum([int(a) * int(b) for (a, b) in all_matches])
            total_sum += product
        return total_sum


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    answer = 2
    return answer


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 161
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 31
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