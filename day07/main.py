from pathlib import Path
import itertools

"""
Idea Part 1:
Try every permutation of operators.
Check if the result of this combination matches the desired result.
"""
OPERATORS = ["+", "*"]


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        total_sum = 0
        for line in file:
            result = int(line.split(":")[0])
            # remove the first " " and the "\n" characters from every line
            operands = [int(number) for number in line.split(":")[1][1:-1].split(" ")]
            permutations = [
                perm
                for perm in itertools.product(OPERATORS, repeat=(len(operands) - 1))
            ]
            for perm in permutations:
                operand_index = 1
                perm_result = operands[0]
                for operator in perm:
                    if operator == "+":
                        perm_result += operands[operand_index]
                        operand_index += 1
                    elif operator == "*":
                        perm_result *= operands[operand_index]
                        operand_index += 1
                    else:
                        print("Edge Case?")
                if perm_result == result:
                    total_sum += result
                    break

        return total_sum


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        pass


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 3749
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
