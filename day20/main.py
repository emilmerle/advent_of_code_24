from pathlib import Path
import itertools

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
RACETRACK = ["E", "."]
WALL = "#"
"""
Idea Part 1:

"""


def algorithm_1(input_filename: str) -> int:
    min_save_time = 100
    cheat_distance = 2
    path = Path(input_filename)
    racetrack = []
    starting_pos = (-1, -1)
    finish_pos = (-1, -1)
    with open(path, "r") as file:
        x_index = 0
        for line in file:
            racetrack.append(line[:-1])
            if "S" in line:
                starting_pos = (x_index, line.index("S"))
            elif "E" in line:
                finish_pos = (x_index, line.index("E"))
            x_index += 1

    race_dict = get_race_dict(racetrack, starting_pos, finish_pos)
    possible_cheat_counter = 0
    possible_cheat_list = []
    for value in race_dict.values():
        for pos in get_cheat_outcomes_part_1(racetrack, value, cheat_distance):
            if (
                pos
                in list(race_dict.values())[
                    list(race_dict.values()).index(value)
                    + cheat_distance
                    + min_save_time :
                ]
            ):
                possible_cheat_counter += 1
                possible_cheat_list.append(pos)

    return possible_cheat_counter


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    min_save_time = 100
    cheat_distance = 20
    path = Path(input_filename)
    racetrack = []
    starting_pos = (-1, -1)
    finish_pos = (-1, -1)
    with open(path, "r") as file:
        x_index = 0
        for line in file:
            racetrack.append(line[:-1])
            if "S" in line:
                starting_pos = (x_index, line.index("S"))
            elif "E" in line:
                finish_pos = (x_index, line.index("E"))
            x_index += 1

    race_dict = get_race_dict(racetrack, starting_pos, finish_pos)
    possible_cheat_counter = 0
    possible_cheat_list = []
    for value in race_dict.values():
        print(f"Current position: {value}")
        for pos in get_cheat_outcomes_part_2(racetrack, value, cheat_distance):
            distance = get_distance(value, pos)
            if (
                pos
                in list(race_dict.values())[
                    list(race_dict.values()).index(value) + distance + min_save_time :
                ]
            ):
                possible_cheat_counter += 1
                possible_cheat_list.append(pos)

    # print(possible_cheat_counter, possible_cheat_list)

    return possible_cheat_counter


# Helping functions
def is_out_of_bounds(position: tuple[int, int], dim_x: int, dim_y: int) -> bool:
    return not (0 <= position[0] < dim_x) or not (0 <= position[1] < dim_y)


def get_distance(first: tuple[int, int], second: tuple[int, int]) -> int:
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def get_next_race_position(
    racetrack: list[str], position: tuple[int, int], previous_pos: tuple[int, int]
) -> tuple[int, int]:
    dim_x, dim_y = len(racetrack), len(racetrack[0])
    for x, y in DIRECTIONS:
        next_position = (position[0] + x, position[1] + y)
        if not is_out_of_bounds(next_position, dim_x, dim_y):
            if (
                next_position != previous_pos
                and racetrack[next_position[0]][next_position[1]] in RACETRACK
            ):
                return next_position


def get_race_dict(
    racetrack: list[str], starting_pos: tuple[int, int], finish_pos: tuple[int, int]
) -> dict:
    race_dict = {0: starting_pos}
    prev_pos = starting_pos
    length = 0
    current_pos = starting_pos
    while current_pos != finish_pos:
        length += 1
        temp_pos = current_pos
        current_pos = get_next_race_position(racetrack, current_pos, prev_pos)
        race_dict[length] = current_pos
        prev_pos = temp_pos
    return race_dict


def get_race_length(race_dict: dict) -> int:
    return len(race_dict) - 1


def get_cheat_outcomes_part_1(
    racetrack: list[str], position: tuple[int, int], cheat_distance: int
) -> list[tuple[int, int]]:
    dim_x, dim_y = len(racetrack), len(racetrack[0])
    possible_outcomes = []
    for i in range(-cheat_distance - 1, cheat_distance + 2):
        for j in range(-cheat_distance - 1, cheat_distance + 2):
            possible_outcomes.append((position[0] + i, position[1] + j))
    possible_outcomes = [
        pos
        for pos in possible_outcomes
        if not is_out_of_bounds(pos, dim_x, dim_y)
        and pos != position
        and get_distance(position, pos) == cheat_distance
    ]
    return possible_outcomes


def get_cheat_outcomes_part_2(
    racetrack: list[str], position: tuple[int, int], cheat_distance: int
) -> list[tuple[int, int]]:
    dim_x, dim_y = len(racetrack), len(racetrack[0])
    possible_outcomes = []
    for i in range(-cheat_distance - 1, cheat_distance + 2):
        for j in range(-cheat_distance - 1, cheat_distance + 2):
            possible_outcomes.append((position[0] + i, position[1] + j))
    possible_outcomes = [
        pos
        for pos in possible_outcomes
        if not is_out_of_bounds(pos, dim_x, dim_y)
        and pos != position
        and get_distance(position, pos) <= cheat_distance
    ]
    return possible_outcomes


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 1
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 0
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
