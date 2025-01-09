import math
from pathlib import Path
import re

"""
Idea Part 1:

"""


def algorithm_1(input_filename: str, is_test: bool) -> int:
    path = Path(input_filename)
    time = 100
    dim_x, dim_y = 101, 103
    if is_test:
        dim_x, dim_y = 11, 7
    position_pattern = r"(\d{1,3}),(\d{1,3})"
    velocity_pattern = r"(-?\d{1,3}),(-?\d{1,3})"
    quadrant_counter = [0,0,0,0]
    with open(path, "r") as file:
        for line in file:
            position_string, velocity_string = line.split(" ")[0], line.split(" ")[1]
            position_matches = re.findall(position_pattern, position_string)
            position = int(position_matches[0][0]), int(position_matches[0][1])
            velocity_matches = re.findall(velocity_pattern, velocity_string)
            velocity = int(velocity_matches[0][0]), int(velocity_matches[0][1])

            final_pos_x = (position[0] + time * velocity[0]) % dim_x
            final_pos_y = (position[1] + time * velocity[1]) % dim_y
            
            cutoff_x = dim_x // 2
            cutoff_y = dim_y // 2
            
            if final_pos_x < cutoff_x:
                if final_pos_y < cutoff_y:
                    quadrant_counter[0] += 1
                elif final_pos_y > cutoff_y:
                    quadrant_counter[1] += 1
            elif final_pos_x > cutoff_x:
                if final_pos_y < cutoff_y:
                    quadrant_counter[2] += 1
                elif final_pos_y > cutoff_y:
                    quadrant_counter[3] += 1

    total_valid_robots = math.prod(quadrant_counter)
    return total_valid_robots
            
            





"""
Idea Part 2:

"""


def algorithm_2(input_filename: str, is_test: bool) -> int:
    path = Path(input_filename)
    time = 100
    dim_x, dim_y = 101, 103
    if is_test:
        dim_x, dim_y = 11, 7
    position_pattern = r"(\d{1,3}),(\d{1,3})"
    velocity_pattern = r"(-?\d{1,3}),(-?\d{1,3})"
    robots = []
    with open(path, "r") as file:
        for line in file:
            position_string, velocity_string = line.split(" ")[0], line.split(" ")[1]
            position_matches = re.findall(position_pattern, position_string)
            position = int(position_matches[0][0]), int(position_matches[0][1])
            velocity_matches = re.findall(velocity_pattern, velocity_string)
            velocity = int(velocity_matches[0][0]), int(velocity_matches[0][1])
            robots.append((position, velocity))

    for index in range(1, 10000):
        time = index
        end_positions= []
        for robot_position, robot_velocity in robots:
            final_pos_x = (robot_position[0] + time * robot_velocity[0]) % dim_x
            final_pos_y = (robot_position[1] + time * robot_velocity[1]) % dim_y
            end_positions.append((final_pos_x, final_pos_y))
        
        if len(set(end_positions)) == len(end_positions):
            return index





# Helping functions


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 12
    algorithm_answer = algorithm_1(filename, True)
    return expected_answer == algorithm_answer


def solve_part1() -> int:
    filename = "./input_files/puzzle.txt"
    algorithm_answer = algorithm_1(filename, False)
    return algorithm_answer


def solve_part2() -> int:
    filename = "./input_files/puzzle.txt"
    algorithm_answer = algorithm_2(filename, False)
    return algorithm_answer


if __name__ == "__main__":
    if test_part1():
        answer = solve_part1()
        print(f"Todays answer of part 1 is {answer}")
    else:
        print("Test of part 1 was not successfull")

    answer = solve_part2()
    print(f"Todays answer of part 2 is {answer}")
