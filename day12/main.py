from pathlib import Path

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

"""
Idea Part 1:

"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    visited_positions = []
    regions = []
    garden = []
    dim_x, dim_y = 0, 0
    with open(path, "r") as file:
        garden = [line[:-1] for line in file]
        dim_x, dim_y = len(garden), len(garden[0])

    for index_x in range(dim_x):
        for index_y in range(dim_y):
            position = (index_x, index_y)
            # Skip current position if already visited
            if position in visited_positions:
                continue

            neighbors = get_whole_region(garden, position)
            visited_positions += neighbors
            current_region = neighbors
            regions.append(current_region)

    total_price = sum(get_price_of_region(garden, region) for region in regions)
    return total_price


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        pass


# Helping functions
def is_out_of_bounds(position: tuple[int, int], dim_x: int, dim_y: int) -> bool:
    return not (0 <= position[0] < dim_x) or not (0 <= position[1] < dim_y)


def get_number_of_same_neighbors(garden: list[str], position: tuple[int, int]) -> int:
    dim_x, dim_y = len(garden), len(garden[0])
    plant_type = garden[position[0]][position[1]]
    number_of_same_neighbors = 0
    for direction in DIRECTIONS:
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if not is_out_of_bounds(next_position, dim_x, dim_y):
            if garden[next_position[0]][next_position[1]] == plant_type:
                number_of_same_neighbors += 1
    return number_of_same_neighbors


def get_same_neighboring_plants(
    garden: list[str], position: tuple[int, int]
) -> list[tuple[int, int]]:
    dim_x, dim_y = len(garden), len(garden[0])
    plant_type = garden[position[0]][position[1]]
    nieghboring_plants = []
    for direction in DIRECTIONS:
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if not is_out_of_bounds(next_position, dim_x, dim_y):
            if garden[next_position[0]][next_position[1]] == plant_type:
                nieghboring_plants.append(next_position)
    return nieghboring_plants


def get_whole_region(
    garden: list[str], position: tuple[int, int]
) -> list[tuple[int, int]]:
    current_region = [position]
    current_neighbors = get_same_neighboring_plants(garden, position)
    while current_neighbors != []:
        next_neighbors = []
        for current_neighbor in current_neighbors:
            current_region.append(current_neighbor)
            next_neighbors += get_same_neighboring_plants(garden, current_neighbor)
        current_neighbors = list(set(next_neighbors) - set(current_region))
    return current_region


def get_price_of_region(garden: list[str], region: list[tuple[int, int]]) -> int:
    area = len(region)
    perimeter = 0
    for position in region:
        borders = 4 - get_number_of_same_neighbors(garden, position)
        perimeter += borders
    return perimeter * area


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test_1.txt"
    expected_answer_1 = 140
    algorithm_answer_1 = algorithm_1(filename)
    filename = "./input_files/test_2.txt"
    expected_answer_2 = 772
    algorithm_answer_2 = algorithm_1(filename)
    filename = "./input_files/test_3.txt"
    expected_answer_3 = 1930
    algorithm_answer_3 = algorithm_1(filename)
    return (
        expected_answer_1 == algorithm_answer_1
        and expected_answer_2 == algorithm_answer_2
        and expected_answer_3 == algorithm_answer_3
    )


def test_part2() -> bool:
    filename = "./input_files/test_1.txt"
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
