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

    first_free_space_index = block_map.index(FREE_SPACE)
    last_file_index = len(block_map) - 1
    while first_free_space_index < last_file_index:
        if block_map[last_file_index] != FREE_SPACE:
            block_map[first_free_space_index] = block_map[last_file_index]
            block_map[last_file_index] = FREE_SPACE
        last_file_index -= 1
        first_free_space_index = block_map.index(FREE_SPACE)
    checksum = calculate_checksum_part1(block_map)
    return checksum


"""
Idea Part 2:
Check the filesystem for blocks with the same length as the file block.
Then move the file block into the free space.
"""


def algorithm_2(input_filename: str) -> int:
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

    # print(block_map)

    first_free_space_index = block_map.index(FREE_SPACE)
    last_file_index = len(block_map) - 1
    while first_free_space_index < last_file_index:
        if block_map[last_file_index] != FREE_SPACE:
            character = block_map[last_file_index]
            block_length = 0
            while block_map[last_file_index] == character:
                block_length += 1
                last_file_index -= 1
            last_file_index += 1
            # print(block_length)

            free_space_index = block_map.index(FREE_SPACE)
            free_space_length = 0
            while (
                free_space_length < block_length and free_space_index < last_file_index
            ):
                if block_map[free_space_index] == FREE_SPACE:
                    free_space_length += 1
                    free_space_index += 1
                else:
                    free_space_length = 0
                    free_space_index += 1
            free_space_starting_index = -1
            if (
                free_space_index <= last_file_index
                and free_space_length >= block_length
            ):
                free_space_starting_index = free_space_index - free_space_length

            # print(first_free_space_index, last_file_index, free_space_starting_index, block_length)
            if free_space_starting_index != -1:
                for index in range(block_length):
                    block_map[free_space_starting_index + index] = character
                    block_map[last_file_index + index] = FREE_SPACE
            # print(block_map)

        last_file_index -= 1
        first_free_space_index = block_map.index(FREE_SPACE)
    checksum = calculate_checksum_part2(block_map)
    return checksum


# Helping functions
def calculate_checksum_part1(filesystem: list[str]) -> int:
    total_sum = 0
    for index in range(len(filesystem) - 1):
        if filesystem[index] == FREE_SPACE:
            return total_sum
        else:
            total_sum = total_sum + index * int(filesystem[index])
    return total_sum


def calculate_checksum_part2(filesystem: list[str]) -> int:
    total_sum = 0
    for index in range(len(filesystem) - 1):
        if filesystem[index] == FREE_SPACE:
            continue
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
    expected_answer = 2858
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
