from pathlib import Path

"""
Idea Part 1:

"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    a, b, c = 0, 0, 0
    program = []
    with open(path, "r") as file:
        a = int(next(file)[12:-1])
        b = int(next(file)[12:-1])
        c = int(next(file)[12:-1])
        next(file)
        program = [int(number) for number in next(file)[9:-1].split(",")]
    
    print(get_output(0, 2, 8, 0, 0))
    output = ""

    return output


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        pass


# Helping functions
def get_output(instruction: int, operand: int, a: int, b: int, c:int ) -> tuple[int, int, int, str]:
    new_a, new_b, new_c = a, b, c
    output = ""
    match instruction:
        # division
        case 0:
            numerator = a
            denominator = 2**get_combo_operand(operand, a, b, c)
            return (new_a, new_b, new_c, f"{int(numerator/denominator)}")
        # Bitwise XOR
        case 1:
            first = b
            second = operand
            return (new_a, first | second, new_c, "")
        # Combo operand modulo 8
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass

    return (new_a, new_b, new_c, output)

def get_combo_operand(operand: int, a: int, b: int, c: int) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c

# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = "4,6,3,5,6,3,5,2,1,0"
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
