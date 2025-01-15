import os
"""
Idea Part 1:

"""


def algorithm_1(input_filename: str) -> int:
    a, b, c = 0, 0, 0
    program = []
    with open(input_filename, "r") as file:
        a = int(next(file)[12:-1])
        b = int(next(file)[12:-1])
        c = int(next(file)[12:-1])
        next(file)
        program = [int(number) for number in next(file)[9:].split(",")]

    output = run_program(program, a, b, c)

    return output


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    with open(input_filename, "r") as file:
        pass


# Helping functions
def run_program(program: list[int], a: int, b: int, c: int) -> str:
    instruction_counter = 0
    output = ""
    new_a, new_b, new_c = a, b, c
    while instruction_counter <= len(program) - 2:
        new_a, new_b, new_c, step_output, instruction_counter = get_output(
            program[instruction_counter],
            program[instruction_counter + 1],
            new_a,
            new_b,
            new_c,
            instruction_counter,
        )
        if step_output != "":
            output = output + "," + step_output

    return output[1:]


def get_output(
    instruction: int, operand: int, a: int, b: int, c: int, ins_counter: int
) -> tuple[int, int, int, str, int]:
    new_a, new_b, new_c = a, b, c
    output = ""
    match instruction:
        # division
        case 0:
            numerator = a
            denominator = 2 ** get_combo_operand(operand, a, b, c)
            return (int(numerator / denominator), new_b, new_c, "", ins_counter + 2)
        # Bitwise XOR
        case 1:
            first = b
            second = operand
            return (new_a, first ^ second, new_c, "", ins_counter + 2)
        # Combo operand modulo 8
        case 2:
            return (
                new_a,
                get_combo_operand(operand, a, b, c) % 8,
                new_c,
                "",
                ins_counter + 2,
            )
        # Jump
        case 3:
            if a == 0:
                return (new_a, new_b, new_c, "", ins_counter + 2)
            return (new_a, new_b, new_c, "", operand)
        # Bitwise XOR
        case 4:
            first = b
            second = c
            return (new_a, first ^ second, new_c, "", ins_counter + 2)
        # Modulo 8
        case 5:
            return (
                new_a,
                new_b,
                new_c,
                f"{get_combo_operand(operand, a, b, c) % 8}",
                ins_counter + 2,
            )
        # division
        case 6:
            numerator = a
            denominator = 2 ** get_combo_operand(operand, a, b, c)
            return (new_a, int(numerator / denominator), new_c, "", ins_counter + 2)
        # division
        case 7:
            numerator = a
            denominator = 2 ** get_combo_operand(operand, a, b, c)
            return (new_a, new_b, int(numerator / denominator), "", ins_counter + 2)

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
dirname = os.path.dirname(__file__)
def test_part1() -> bool:
    filename = os.path.join(dirname, "./input_files/test.txt")
    expected_answer = "4,6,3,5,6,3,5,2,1,0"
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
