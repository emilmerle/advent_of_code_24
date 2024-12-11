from pathlib import Path

"""
Idea Part 1:
Do 25 times:
Apply the rules for every stone and concatenate the returning lists of stones.
In the end, count the number of stones.
"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        stones = [int(number) for number in next(file).split(" ")]
        for i in range(25):
            stones = blink(stones)
        return len(stones)


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        pass


# Helping functions
def blink(stones: list[int]) -> list[int]:
    next_stones = []
    for stone in stones:
        next_stones += apply_rules(stone)
    return next_stones


def apply_rules(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    else:
        string_stone = str(stone)
        if len(string_stone) % 2 == 0:
            return [
                int(string_stone[: len(string_stone) // 2]),
                int(string_stone[len(string_stone) // 2 :]),
            ]
        else:
            return [stone * 2024]


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 55312
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
