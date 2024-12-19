from collections import defaultdict
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
Same approach as part 1 is not possible, because the number of stones will be too large.
Idea 1:
Do not calculate every blink, but calculate number of stones after 75 times separately (with other rules).
Not really possible, there are no trivial rules to calculate only the number of stones.
Idea 2:
Keep track of how often every stone is in the list.
Then, calculate the next stones only once for every unique stone in the current blink.
The defaultdict(int) is a dictionary, where you can calculate with values of keys without explicitly setting a value for the key before.
"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        stones = {int(number): 1 for number in next(file).split(" ")}
        for _ in range(1, 75 + 1):
            next_stones = defaultdict(int)
            for stone, amount in stones.items():
                for next_stone in apply_rules(stone):
                    next_stones[next_stone] += amount
            stones = next_stones

        return sum(stones.values())


# Helping functions
def blink(stones: list[int]) -> list[int]:
    next_stones = []
    for stone in stones:
        next_stones += apply_rules(stone)
    return next_stones


def apply_rules(stone: int) -> list[int]:
    next_stones = []
    if stone == 0:
        next_stones = [1]
    else:
        string_stone = str(stone)
        if len(string_stone) % 2 == 0:
            next_stones = [
                int(string_stone[: len(string_stone) // 2]),
                int(string_stone[len(string_stone) // 2 :]),
            ]
        else:
            next_stones = [stone * 2024]
    return next_stones


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

    answer = solve_part2()
    print(f"Todays answer of part 2 is {answer}")
