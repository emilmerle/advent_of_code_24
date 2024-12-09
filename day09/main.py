from pathlib import Path

"""
Idea Part 1:
Build the filesystem as a list like the problem specifies.
Then move the last digit to the first free space until the last digit is in front of the first free space.
"""
FREE_SPACE = "."


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    block_map = []
    with open(path, "r") as file:
        input = next(file)[:-1]
        for index in range(len(input)):
            character = input[index]
            if index % 2 == 0:
                file_id = index // 2
                block_map = block_map + int(character) * [file_id]

            elif index % 2 == 1:
                block_map = block_map + int(character) * [FREE_SPACE]
            else:
                print("Edge Case")

    first_free_space_index = block_map.index(FREE_SPACE)
    last_file_index = len(block_map) - 1
    while first_free_space_index < last_file_index:
        if block_map[last_file_index] != FREE_SPACE:
            block_map[first_free_space_index] = block_map[last_file_index]
            block_map[last_file_index] = FREE_SPACE
        last_file_index -= 1
        first_free_space_index = block_map.index(FREE_SPACE)
    checksum = calculate_checksum(block_map)
    return checksum


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        pass


# Helping functions
def calculate_checksum(filesystem: list[str]) -> int:
    total_sum = 0
    for index in range(len(filesystem) - 1):
        if filesystem[index] == FREE_SPACE:
            return total_sum
        else:
            total_sum = total_sum + index * int(filesystem[index])
    return total_sum


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 1928
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
