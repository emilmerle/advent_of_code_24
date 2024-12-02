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
            if check_report_part1(report):
                safe_reports += 1

        return safe_reports

    answer = safe_reports
    return answer

"""
Idea Part 2:

"""
def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as f:
        safe_reports = 0
        for line in f:
            report = [int(x) for x in line.split()]
            is_report_safe = check_report_part2(report)
            print(report, is_report_safe)
            if is_report_safe:
                safe_reports += 1

        return safe_reports

    answer = safe_reports
    return answer
    
    
    
    
    
    answer = safe_reports
    return answer



# Helping functions:
"""
Check if levels are increasing or decreasing with the first two elements.
Then check if all other differences have the same sign and difference under 4 with check_two().
Then check if the list contains only True values with all().
"""
def check_report_part1(report: list) -> bool:
    reverse = True if report[0] - report[1] > 0 else False
    is_safe_report = all(
        [
            check_two(report[index], report[index + 1], reverse)
            for index in range(len(report) - 1)
        ]
    )
    return is_safe_report


def check_two(first: int, second: int, reverse: bool) -> bool:
    if not reverse:
        return True if -4 < first - second < 0 else False
    else:
        return True if 4 > first - second > 0 else False

def check_report_part2(report: list) -> bool:
    reverse = is_reverse(report)
    index = 0
    number_removed = False
    while index < len(report) - 2:
        if check_two(report[index], report[index + 1], reverse):
            index += 1
        elif number_removed:
            return False
        else:
            if index == 0:
                index += 1
                continue
            if check_two(report[index], report[index + 2], reverse):
                number_removed = True
                index += 2
            else:
                return False
            
        

    if not check_two(report[-2], report[-1], reverse):
        if number_removed:
            return False
        
    if not check_two(report[0], report[1], reverse) and not number_removed:
        return True

    return True

# This checks if the list is "sorted" in reverse direction or not
# Could lead to errors in special cases!!!
def is_reverse(report: list) -> bool:
    differences_list = [report[index] - report[index + 1] for index in range(len(report) - 1)]
    return True if sum(differences_list) > 0 else False




# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 2
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 44
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
