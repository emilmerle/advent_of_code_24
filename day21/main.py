from pathlib import Path

"""
Idea Part 1:

"""
ACTIVATE = "A"
UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

NUMPAD = {
    "0": (0, 1),
    "A": (0, 2),
    "1": (1, 0),
    "2": (1, 1),
    "3": (1, 2),
    "4": (2, 0),
    "5": (2, 1),
    "6": (2, 2),
    "7": (3, 0),
    "8": (3, 1),
    "9": (3, 2),
}

KEYPAD = {
    "A": (1, 2),
    "<": (0, 0),
    "v": (0, 1),
    ">": (0, 2),
    "^": (1, 1)
}

def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    codes = []
    with open(path, "r") as file:
        codes = [line[:-1] for line in file]

    total_sum = 0
    for code in codes:
        print(code)
        presses = solve_code_part_1(code)
        temp_sum = len(presses) * get_numeric_part(code)
        total_sum += temp_sum
        print(len(presses), get_numeric_part(code))
    
    print(total_sum)
    return total_sum


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        pass


# Helping functions
def get_numeric_part(code: str) -> int:
    return int(code[:3])

def get_keypresses_for_code(code: str, keypad: dict) -> str:
    current_pos = keypad[ACTIVATE]
    keypresses = ""
    while code != "":
        next_key_pos = keypad[code[0]]
        distance_vector = get_distance_vector(current_pos, next_key_pos)
        keystrokes = get_keypresses_for_key(distance_vector)

        match code[0]:
            case "1" | "4" | "7":
                if "<^" in keystrokes:
                    keystrokes.replace("<^", "^<")
            case "0":
                if "v>" in keystrokes:
                    keystrokes.replace("v>", ">v")
            case "A":
                if "v>" in keystrokes:
                    keystrokes.replace("v>", ">v")
                elif "^>" in keystrokes:
                    keystrokes.replace("^>", ">^")
            case "<":
                if "<v" in keystrokes:
                    keystrokes.replace("<v", "v<")
            case "^":
                if "^>" in keystrokes:
                    keystrokes.replace("^>", ">^")

        


        # print(distance_vector, current_pos, next_key_pos, keystrokes)
        keypresses = keypresses + keystrokes + ACTIVATE
        current_pos = next_key_pos
        code = code[1:]
    return keypresses


def get_keypresses_for_key(distance_vector: tuple[int, int]) -> str:
    keypresses = ""
    if distance_vector[1] > 0:
        keypresses = keypresses + (distance_vector[1] * LEFT)
    if distance_vector[1] < 0:
        keypresses = keypresses + (abs(distance_vector[1]) * RIGHT)
    if distance_vector[0] > 0:
        keypresses = keypresses + (distance_vector[0] * DOWN)
    if distance_vector[0] < 0:
        keypresses = keypresses + (abs(distance_vector[0]) * UP)
    return keypresses
        


def get_distance_vector(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
    return (first[0] - second[0], first[1] - second[1])


def solve_code_part_1(code: str) -> str:
    presses = get_keypresses_for_code(code, NUMPAD)
    print(presses)
    presses = get_keypresses_for_code(presses, KEYPAD)
    print(presses)
    presses = get_keypresses_for_code(presses, KEYPAD)
    print(presses)
    return presses



# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 126384
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
