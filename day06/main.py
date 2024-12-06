from pathlib import Path

"""
Idea Part 1:
Retrace the line the guard walks and mark every step with a symbol.
Then, count the symbols after the guard leaves the map.
"""
UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        # Remove the "\n" character from every line end
        lab_map = [list(line[:-1]) for line in file]
        dim_x, dim_y = len(lab_map), len(lab_map[0])
        starting_pos = (0, 0)
        for index_x in range(dim_x - 1):
            if "^" in lab_map[index_x]:
                starting_pos = (index_x, lab_map[index_x].index("^"))

        current_direction = UP
        current_position = starting_pos
        while 0 <= current_position[0] < dim_x and 0 <= current_position[1] < dim_y:
            lab_map, current_position, current_direction = move(
                lab_map, current_position, current_direction, dim_x, dim_y
            )

        visited_spaces = 0
        for symbol_list in lab_map:
            visited_spaces += symbol_list.count("X")

        return visited_spaces


def move(
    lab_map: list,
    position: tuple[int, int],
    direction: tuple[int, int],
    dim_x: int,
    dim_y: int,
) -> tuple[list, tuple[int, int], tuple[int, int]]:

    if (
        not 0 <= position[0] + direction[0] < dim_x
        or not 0 <= position[1] + direction[1] < dim_y
    ):
        lab_map[position[0]][position[1]] = "X"
        return (lab_map, (-1, -1), (0, 0))

    new_direction = direction
    new_lab_map = lab_map
    new_position = position
    # Turn if looking into an object
    if lab_map[position[0] + direction[0]][position[1] + direction[1]] == "#":
        new_direction = get_next_direction(direction)

    # Move and mark old position with "X" if not looking into an object
    elif not lab_map[position[0] + direction[0]][position[1] + direction[1]] == "#":
        new_lab_map[position[0]][position[1]] = "X"
        new_position = (position[0] + direction[0], position[1] + direction[1])
    else:
        print("Edge Case?")
    return (new_lab_map, new_position, new_direction)


def get_next_direction(position: tuple[int, int]) -> tuple[int, int]:
    if position == (-1, 0):
        return (0, 1)
    elif position == (0, 1):
        return (1, 0)
    elif position == (1, 0):
        return (0, -1)
    elif position == (0, -1):
        return (-1, 0)


"""
Idea Part 2:

"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        pass


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 41
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
