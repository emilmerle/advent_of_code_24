import os
"""
Idea Part 1:

"""


def algorithm_1(input_filename: str) -> int:
    with open(input_filename, "r") as file:
        pass


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    with open(input_filename, "r") as file:
        pass


# Helping functions


# Testing and solving functions
dirname = os.path.dirname(__file__)
def test_part1() -> bool:
    filename = os.path.join(dirname, "./input_files/test.txt")
    expected_answer = 11
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = os.path.join(dirname, "./input_files/test.txt")
    expected_answer = 31
    algorithm_answer = algorithm_2(filename)
    return expected_answer == algorithm_answer


def solve_part1() -> int:
    filename = os.path.join(dirname, "./input_files/puzzle.txt")
    algorithm_answer = algorithm_1(filename)
    return algorithm_answer


def solve_part2() -> int:
    filename = os.path.join(dirname, "./input_files/puzzle.txt")
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
