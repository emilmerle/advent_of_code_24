from pathlib import Path
import itertools

"""
Idea Part 1:
Create a dictionary with all frequencies and its locations.
Calculate distance vector and the antinodes.
Count unique locations of the antinodes.
"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    antenna_dictionary = {}
    with open(path, "r") as file:
        line_index = 0
        dim_x, dim_y = 0, 0
        for line in file:
            char_index = 0
            for char in line[:-1]:
                if char != "." and char != "\n":
                    if char in antenna_dictionary:
                        antenna_dictionary[char].append((line_index, char_index))
                    else:
                        antenna_dictionary[char] = [(line_index, char_index)]

                char_index += 1
                if line_index == 0:
                    dim_y = char_index
            line_index += 1

        dim_x = line_index

    # print(antenna_dictionary)
    unique_antinode_locations = []
    for char in antenna_dictionary:
        permutations = [
            perm
            for perm in itertools.product(antenna_dictionary[char], repeat=2)
            if perm[0] != perm[1]
        ]
        for perm in permutations:
            distance = calculate_distance(perm[0], perm[1])
            position_1 = (perm[0][0] - distance[0], perm[0][1] - distance[1])
            position_2 = (perm[1][0] + distance[0], perm[1][1] + distance[1])
            if (
                is_in_bounds(position_1, dim_x, dim_y)
                and position_1 not in unique_antinode_locations
            ):
                unique_antinode_locations.append(position_1)
            if (
                is_in_bounds(position_2, dim_x, dim_y)
                and position_2 not in unique_antinode_locations
            ):
                unique_antinode_locations.append(position_2)

    return len(unique_antinode_locations)


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    antenna_dictionary = {}
    with open(path, "r") as file:
        line_index = 0
        dim_x, dim_y = 0, 0
        for line in file:
            char_index = 0
            for char in line[:-1]:
                if char != "." and char != "\n":
                    if char in antenna_dictionary:
                        antenna_dictionary[char].append((line_index, char_index))
                    else:
                        antenna_dictionary[char] = [(line_index, char_index)]

                char_index += 1
                if line_index == 0:
                    dim_y = char_index
            line_index += 1

        dim_x = line_index

    # print(antenna_dictionary)
    unique_antinode_locations = []
    for char in antenna_dictionary:
        permutations = [
            perm
            for perm in itertools.product(antenna_dictionary[char], repeat=2)
            if perm[0] != perm[1]
        ]
        for perm in permutations:
            distance = calculate_distance(perm[0], perm[1])
            position_1 = (perm[0][0] - distance[0], perm[0][1] - distance[1])
            position_2 = (perm[1][0] + distance[0], perm[1][1] + distance[1])
            if (
                is_in_bounds(position_1, dim_x, dim_y)
                and position_1 not in unique_antinode_locations
            ):
                unique_antinode_locations.append(position_1)
            if (
                is_in_bounds(position_2, dim_x, dim_y)
                and position_2 not in unique_antinode_locations
            ):
                unique_antinode_locations.append(position_2)

    return len(unique_antinode_locations)


# Helping functions
def is_in_bounds(position: tuple[int, int], dim_x, dim_y) -> bool:
    return 0 <= position[0] < dim_x and 0 <= position[1] < dim_y


def calculate_distance(
    first: tuple[int, int], second: tuple[int, int]
) -> tuple[int, int]:
    return (second[0] - first[0], second[1] - first[1])


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 14
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
