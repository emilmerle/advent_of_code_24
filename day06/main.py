from pathlib import Path
from copy import deepcopy

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

        current_direction = (-1, 0)
        current_position = starting_pos
        while 0 <= current_position[0] < dim_x and 0 <= current_position[1] < dim_y:
            lab_map, current_position, current_direction = move(
                lab_map, current_position, current_direction
            )

        visited_spaces = 0
        for symbol_list in lab_map:
            visited_spaces += symbol_list.count("X")

        return visited_spaces


"""
Idea Part 2:
Idea 1:
Save all visited position with the direction we moved then.
Test if we cross a position we already visited.
If we do: test if the old direction is one turn away from the current direction.
Then, the next position we would move to could also be an obstacle.
THIS DOES NOT COVER EVERY CASE!!!

Idea 2:
Check for every existing obstacle if two other needed obstacles exist in the right positions.
If yes, we could place a third one.
Then only count these where the players would walk over.
THIS DOES NOT COVER THE CASE, WHEN THE LOOP HAS MORE THAN 4 CORNERS!!!

Idea 3:
In every step, place an obstacle in front and check for a loop.
STILL DOES NOT WORK!!!
A comment on Reddit stated: Obstacles must be placed before the guard moves.
Now, do not start from the current position but from the starting position to detect loops.
This solves the problem.
"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        # Remove the "\n" character from every line end
        lab_map = [list(line[:-1]) for line in file]
        dim_x, dim_y = len(lab_map), len(lab_map[0])
        starting_pos = (0, 0)
        for index_x in range(dim_x - 1):
            if "^" in lab_map[index_x]:
                starting_pos = (index_x, lab_map[index_x].index("^"))

        direction = (-1, 0)
        current_position = deepcopy(starting_pos)

        obstacle_positions = []
        while not is_out_of_bounds(lab_map, current_position):

            # Create a deepcopy of the map, position and direction
            # Place and obstacle right in front of the player
            # Then check if the map has loops
            # Do not start from the current position but the starting position!
            potential_map = deepcopy(lab_map)
            potential_position = deepcopy(current_position)
            potential_direction = deepcopy(direction)
            potential_map = place_obstacle_in_front(
                potential_map, potential_position, potential_direction
            )
            loop = has_loop(potential_map, starting_pos, (-1, 0))
            if loop:
                obstacle_position = (
                    potential_position[0] + potential_direction[0],
                    potential_position[1] + potential_direction[1],
                )
                obstacle_positions.append(obstacle_position)

            lab_map, current_position, direction = move(
                lab_map, current_position, direction
            )

        # Only count unique obstacle positions
        return len(set(obstacle_positions))


def has_loop(
    lab_map: list, position: tuple[int, int], direction: tuple[int, int]
) -> bool:

    temp_map = deepcopy(lab_map)
    temp_position = deepcopy(position)
    temp_direction = deepcopy(direction)

    visited_positions = {}
    while not is_out_of_bounds(temp_map, temp_position):
        # Stuck in loop if the current position was already visited with the same direction
        if temp_position in visited_positions:
            if temp_direction in visited_positions[temp_position]:
                # print(f"Was already at position {current_position} with direction {current_direction}")
                return True
            else:
                visited_positions[temp_position].append(temp_direction)
        elif temp_position not in visited_positions:
            visited_positions[temp_position] = [temp_direction]

        # Actual Move
        temp_map, temp_position, temp_direction = move(
            temp_map, temp_position, temp_direction
        )

    return False


# Helping functions
def place_obstacle_in_front(
    lab_map: list, position: tuple[int, int], direction: tuple[int, int]
) -> list[list]:
    next_position = (position[0] + direction[0], position[1] + direction[1])
    # if the next position would not be in bounds, just return the original map
    if is_out_of_bounds(lab_map, next_position):
        return lab_map
    # else place the obstacle in front
    lab_map = place_obstacle(lab_map, next_position)
    return lab_map


def move(
    lab_map: list[list],
    position: tuple[int, int],
    direction: tuple[int, int],
) -> tuple[list[list], tuple[int, int], tuple[int, int]]:
    next_position = (position[0] + direction[0], position[1] + direction[1])

    if is_out_of_bounds(lab_map, next_position):
        lab_map = mark_position(lab_map, position)
        return (lab_map, (-1, -1), (0, 0))

    # Turn if looking into an object
    elif is_obstacle(lab_map, next_position):
        direction = get_next_direction(direction)

    # Move and mark old position with "X" if not looking into an object
    else:
        lab_map = mark_position(lab_map, position)
        position = next_position
    return (lab_map, position, direction)


def is_obstacle(lab_map: list[list], position: tuple[int, int]) -> bool:
    return lab_map[position[0]][position[1]] == "#"


def is_out_of_bounds(lab_map: list[list], position: tuple[int, int]) -> bool:
    dim_x, dim_y = len(lab_map), len(lab_map[0])
    return not 0 <= position[0] < dim_x or not 0 <= position[1] < dim_y


def mark_position(lab_map: list[list], position: tuple[int, int]) -> list[list]:
    lab_map[position[0]][position[1]] = "X"
    return lab_map


def place_obstacle(lab_map: list[list], position: tuple[int, int]) -> list[list]:
    lab_map[position[0]][position[1]] = "#"
    return lab_map


def get_next_direction(position: tuple[int, int]) -> tuple[int, int]:
    if position == (-1, 0):
        return (0, 1)
    elif position == (0, 1):
        return (1, 0)
    elif position == (1, 0):
        return (0, -1)
    elif position == (0, -1):
        return (-1, 0)


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test_1.txt"
    expected_answer = 41
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test_2.txt"
    expected_answer = 6
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
