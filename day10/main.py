from pathlib import Path

"""
Idea Part 1:
Search for every trailhead.
Then start searching how many 9-positions can be reached.
"""
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        topographic_map = []
        for line in file:
            topographic_map.append(line[:-1])

    total_score_sum = 0
    dim_x, dim_y = len(topographic_map), len(topographic_map[0])
    for index_x in range(dim_x):
        trailhead_positions = [
            (index_x, n) for (n, e) in enumerate(topographic_map[index_x]) if e == "0"
        ]
        for trailhead_position in trailhead_positions:
            trailhead_score = calculate_trailhead_score_part1(
                topographic_map, trailhead_position
            )
            total_score_sum += trailhead_score
    return total_score_sum


"""
Idea Part 2:
Search for every trailhead.
Then start searching how many unique trails can reach a 9-position
"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        topographic_map = []
        for line in file:
            topographic_map.append(line[:-1])

    total_score_sum = 0
    dim_x, dim_y = len(topographic_map), len(topographic_map[0])
    for index_x in range(dim_x):
        trailhead_positions = [
            (index_x, n) for (n, e) in enumerate(topographic_map[index_x]) if e == "0"
        ]
        for trailhead_position in trailhead_positions:
            trailhead_score = calculate_trailhead_score_part2(
                topographic_map, trailhead_position
            )
            total_score_sum += trailhead_score
    return total_score_sum


# Helping functions
def is_out_of_bounds(position: tuple[int, int], dim_x: int, dim_y: int) -> bool:
    return not 0 <= position[0] < dim_x or not 0 <= position[1] < dim_y


def get_next_positions(
    topographic_map: list[str], position: tuple[int, int]
) -> list[tuple[int, int]]:
    dim_x, dim_y = len(topographic_map), len(topographic_map[0])
    next_positions = []
    current_score = int(topographic_map[position[0]][position[1]])
    if current_score == 9:
        return [(-1, -1)]
    for direction in DIRECTIONS:
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if not is_out_of_bounds(next_position, dim_x, dim_y):
            if (
                int(topographic_map[next_position[0]][next_position[1]])
                == current_score + 1
            ):
                next_positions.append(next_position)

    return next_positions


def calculate_trailhead_score_part1(
    topographic_map: list[str], position: tuple[int, int]
) -> int:
    trailhead_score = 0
    next_positions = get_next_positions(topographic_map, position)
    while next_positions != []:
        print(next_positions)
        new_positions = []
        for next_position in next_positions:
            new_positions += get_next_positions(topographic_map, next_position)

        end_positions = new_positions.count((-1, -1))
        trailhead_score += end_positions

        # we need to remove duplicate positions here
        new_positions = list(set(new_positions))
        if (-1, -1) in new_positions:
            new_positions.remove((-1, -1))
        next_positions = new_positions
    return trailhead_score


def calculate_trailhead_score_part2(
    topographic_map: list[str], position: tuple[int, int]
) -> int:
    trailhead_score = 0
    next_positions = get_next_positions(topographic_map, position)
    while next_positions != []:
        new_positions = []
        for next_position in next_positions:
            new_positions += get_next_positions(topographic_map, next_position)

        end_positions = new_positions.count((-1, -1))
        trailhead_score += end_positions

        # we do not need to remove duplicate positions here
        # new_positions = list(set(new_positions))
        if (-1, -1) in new_positions:
            new_positions.remove((-1, -1))
        next_positions = new_positions
    return trailhead_score


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 36
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 81
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
