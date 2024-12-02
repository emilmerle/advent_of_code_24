from pathlib import Path

"""
Idea Part 1:
Iterate over every line (report).
Check if the report is safe.
Increase counter if it is safe.

Possibility 1:
Check if the levels of the reports are sorted.
Then check the difference of every pair of adjacent numbers.
-> at least two iterations needed

Possibilty 2:
Check for difference and sorting in one iteration?
"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as f:
        safe_reports = 0
        for line in f:
            report = [int(x) for x in line.split()]
            if is_safe_report(report):
                safe_reports += 1
        return safe_reports


"""
Idea Part 2:
For every report, try removing one number (level) at a time and check if the report is safe,
until a safe report is found, otherwise, the report is not safe.
"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as f:
        safe_reports = 0
        for line in f:
            report = [int(x) for x in line.split()]
            if check_report_part2(report):
                safe_reports += 1
        return safe_reports


# Helping functions:
def check_report_part2(report: list) -> bool:
    for index in range(len(report)):
        if is_safe_report(report[:index] + report[index + 1 :]):
            return True

    return False


"""
Check if levels are increasing or decreasing with the first two elements.
Then check if all other differences have the same sign and difference under 4 with check_two().
Then check if the list contains only True values with all().
"""


def is_safe_report(report: list) -> bool:
    reverse = is_reverse(report)
    is_safe_report = all(
        [
            check_two(report[index], report[index + 1], reverse)
            for index in range(len(report) - 1)
        ]
    )
    return is_safe_report


# This checks if two numbers are "sorted" and if the difference is under 4
def check_two(first: int, second: int, reverse: bool) -> bool:
    if not reverse:
        return True if -4 < first - second < 0 else False
    else:
        return True if 4 > first - second > 0 else False


# This checks if the list is "sorted" in reverse direction or not
def is_reverse(report: list) -> bool:
    differences_list = [
        report[index] - report[index + 1] for index in range(len(report) - 1)
    ]
    return True if sum([-1 if x < 0 else 1 for x in differences_list]) > 0 else False


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 2
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 4
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
