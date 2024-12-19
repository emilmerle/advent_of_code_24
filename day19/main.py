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
"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        available_patterns = [pattern for pattern in next(file)[:-1].split(", ")]
        next(file)
        not_possible = 0
        for line in file:
            desired_pattern = line[:-1]
            while desired_pattern != "":
                index = 1
                while True:
                    if index > len(desired_pattern):
                        not_possible += 1
                        desired_pattern = ""
                        break
                    searched_for = desired_pattern[:index]
                    print(searched_for)
                    if searched_for in available_patterns:
                        desired_pattern = desired_pattern[index:]
                        print(desired_pattern)
                        break
                    index += 1
            print(not_possible)
                




"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        pass


# Helping functions


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 6
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
