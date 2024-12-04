from pathlib import Path


"""
Idea Part 1:
Search for every "X" in the file.
Search all possible positions for the word "XMAS" from that starting "X".
THIS IS NOT PRETTY!!! :(
"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        # cut "\n" from every line
        letters = [line[:-1] for line in file]
        dim_x, dim_y = len(letters), len(letters[0])

        total_xmas_count = 0
        for index_x in range(dim_x):
            for index_y in range(dim_y):
                if letters[index_x][index_y] == "X":
                    xmas_count = [
                        search_xmas_right(letters, index_x, index_y, dim_y),
                        search_xmas_right_down(letters, index_x, index_y, dim_x, dim_y),
                        search_xmas_down(letters, index_x, index_y, dim_x),
                        search_xmas_left_down(letters, index_x, index_y, dim_x),
                        search_xmas_left(letters, index_x, index_y),
                        search_xmas_left_up(letters, index_x, index_y),
                        search_xmas_up(letters, index_x, index_y),
                        search_xmas_right_up(letters, index_x, index_y, dim_y),
                    ].count(True)
                    total_xmas_count += xmas_count

        return total_xmas_count


"""
Idea Part 2:
Search for every "A" in the file because "A" is always the middle of the X.
Check if the edges of the X are filled with the correct letters in one of the 4 possible arrangements.
"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        # cut "\n" from every line
        letters = [line[:-1] for line in file]
        dim_x, dim_y = len(letters), len(letters[0])

        total_mas_count = 0
        for index_x in range(dim_x):
            for index_y in range(dim_y):
                if letters[index_x][index_y] == "A":
                    if search_mas(letters, index_x, index_y, dim_x, dim_y):
                        total_mas_count += 1
        return total_mas_count


# Helping functions
# Functions for determining if, from a given x, y position, the word "XMAS" is present
def search_xmas_right(letters: list, index_x: int, index_y: int, dim_y: int) -> bool:
    if index_y <= dim_y - 4:
        return (
            letters[index_x][index_y]
            + letters[index_x][index_y + 1]
            + letters[index_x][index_y + 2]
            + letters[index_x][index_y + 3]
            == "XMAS"
        )
    return False


def search_xmas_left(letters: list, index_x: int, index_y: int) -> bool:
    if index_y >= 0 + 3:
        return (
            letters[index_x][index_y]
            + letters[index_x][index_y - 1]
            + letters[index_x][index_y - 2]
            + letters[index_x][index_y - 3]
            == "XMAS"
        )
    return False


def search_xmas_up(letters: list, index_x: int, index_y: int) -> bool:
    if index_x >= 0 + 3:
        return (
            letters[index_x][index_y]
            + letters[index_x - 1][index_y]
            + letters[index_x - 2][index_y]
            + letters[index_x - 3][index_y]
            == "XMAS"
        )
    return False


def search_xmas_down(letters: list, index_x: int, index_y: int, dim_x: int) -> bool:
    if index_x <= dim_x - 4:
        return (
            letters[index_x][index_y]
            + letters[index_x + 1][index_y]
            + letters[index_x + 2][index_y]
            + letters[index_x + 3][index_y]
            == "XMAS"
        )
    return False


def search_xmas_right_down(
    letters: list, index_x: int, index_y: int, dim_x: int, dim_y: int
) -> bool:
    if index_x <= dim_x - 4 and index_y <= dim_y - 4:
        return (
            letters[index_x][index_y]
            + letters[index_x + 1][index_y + 1]
            + letters[index_x + 2][index_y + 2]
            + letters[index_x + 3][index_y + 3]
            == "XMAS"
        )
    return False


def search_xmas_left_down(
    letters: list, index_x: int, index_y: int, dim_x: int
) -> bool:
    if index_x <= dim_x - 4 and index_y >= 0 + 3:
        return (
            letters[index_x][index_y]
            + letters[index_x + 1][index_y - 1]
            + letters[index_x + 2][index_y - 2]
            + letters[index_x + 3][index_y - 3]
            == "XMAS"
        )
    return False


def search_xmas_left_up(letters: list, index_x: int, index_y: int) -> bool:
    if index_x >= 0 + 3 and index_y >= 0 + 3:
        return (
            letters[index_x][index_y]
            + letters[index_x - 1][index_y - 1]
            + letters[index_x - 2][index_y - 2]
            + letters[index_x - 3][index_y - 3]
            == "XMAS"
        )
    return False


def search_xmas_right_up(letters: list, index_x: int, index_y: int, dim_y) -> bool:
    if index_x >= 0 + 3 and index_y <= dim_y - 4:
        return (
            letters[index_x][index_y]
            + letters[index_x - 1][index_y + 1]
            + letters[index_x - 2][index_y + 2]
            + letters[index_x - 3][index_y + 3]
            == "XMAS"
        )
    return False


# Checking if, from the starting x, y position, the X with the letters "S" and "M" is formed.
def search_mas(letters: list, index_x: int, index_y: int, dim_x: int, dim_y: int):
    # If the A is on the edge of the input, is is not possible to have an X
    if index_x == dim_x - 1 or index_y == dim_y - 1 or index_x == 0 or index_y == 0:
        return False
    # 4 possible arrangements for the 2 S and the 2 M
    else:
        x_edges = (
            letters[index_x - 1][index_y - 1]
            + letters[index_x - 1][index_y + 1]
            + letters[index_x + 1][index_y + 1]
            + letters[index_x + 1][index_y - 1]
        )
        return x_edges in ["MMSS", "MSSM", "SSMM", "SMMS"]


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 18
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 9
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
