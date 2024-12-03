from pathlib import Path
import re


"""
Idea Part 1:
Search the file with Regex to get all mul(X,Y) operations.
"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        data = file.read().replace("\n", "")

        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        all_matches = re.findall(pattern, data)
        total_sum = sum([int(a) * int(b) for (a, b) in all_matches])

        return total_sum


"""
Idea Part 2:
Search the file for all conditional statements and all multiplication statements.
Add them to a list with the position in the file and sort the list by this position.
Then go through the list and "enable/disable multiplication" when a conditional statements is found.
Only add the product to the total sum if multiplication is enabled.
"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        data = file.read().replace("\n", "")

        conditional_pattern = r"do\(\)|don't\(\)"
        multiplication_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        operation_list = []

        # Find all possible multiplications
        all_multplication_matches = re.finditer(multiplication_pattern, data)
        for multiplication_match in all_multplication_matches:
            # match.group(1) and match.group(2) are the factors of the multiplication
            operation_list.append(
                (
                    multiplication_match.start(),
                    int(multiplication_match.group(1)),
                    int(multiplication_match.group(2)),
                )
            )

        # Find all conditional statements
        all_conditional_matches = re.finditer(conditional_pattern, data)
        for conditional_match in all_conditional_matches:
            operation_list.append(
                (conditional_match.start(), conditional_match.group(0))
            )

        # Sort by position of the statement in the file
        operation_list.sort(key=lambda x: x[0])

        mulitplication_enabled = True
        total_sum = 0
        for operation in operation_list:
            # length of 3 -> multiplication statement
            if len(operation) == 3 and mulitplication_enabled:
                total_sum += operation[1] * operation[2]
            # length of 2 -> conditional statement
            elif len(operation) == 2:
                if operation[1].startswith("don't"):
                    mulitplication_enabled = False
                else:
                    mulitplication_enabled = True
            else:
                continue

        return total_sum


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 161
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test_2.txt"
    expected_answer = 48
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
