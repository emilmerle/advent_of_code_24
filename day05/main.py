from pathlib import Path


"""
Idea Part 1:
Create a dictionary with all rules (for every number, enter the previous and the following numbers).
Then go through every number in the updates, and check if any rules are violated.
"""


def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        rules = {}
        correct_update_sum = 0

        for line in file:
            # Rules
            if "|" in line:
                first, second = int(line.split("|")[0]), int(line.split("|")[1])
                if first not in rules:
                    rules[first] = {"previous": [], "following": [second]}
                elif first in rules:
                    rules[first]["following"].append(second)
                else:
                    print("Dictionary error", first, second)

                if second not in rules:
                    rules[second] = {"previous": [first], "following": []}
                elif second in rules:
                    rules[second]["previous"].append(first)
                else:
                    print("Dictionary error", first, second)

            # Updates
            elif "," in line:
                correct_update = True
                numbers = [int(x) for x in line.split(",")]
                for index in range(len(numbers) - 1):
                    for prev_number in numbers[:index]:
                        if prev_number in rules[numbers[index]]["following"]:
                            correct_update = False
                    for followed_number in numbers[index + 1 :]:
                        if followed_number in rules[numbers[index]]["previous"]:
                            correct_update = False

                if correct_update:
                    # Get the middle number of the update and add it to the sum
                    correct_update_sum += numbers[len(numbers) // 2]

        return correct_update_sum


"""
Idea Part 2:
Remove invalid numbers and insert them right before or after the number that was checked.
"""


def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as file:
        rules = {}
        corrected_update_sum = 0

        for line in file:
            # Rules
            if "|" in line:
                first, second = int(line.split("|")[0]), int(line.split("|")[1])
                if first not in rules:
                    rules[first] = {"previous": [], "following": [second]}
                elif first in rules:
                    rules[first]["following"].append(second)
                else:
                    print("Dictionary error", first, second)

                if second not in rules:
                    rules[second] = {"previous": [first], "following": []}
                elif second in rules:
                    rules[second]["previous"].append(first)
                else:
                    print("Dictionary error", first, second)

            # Updates
            elif "," in line:
                correct_update = True
                numbers = [int(x) for x in line.split(",")]
                for index in range(len(numbers) - 1):
                    for prev_number in numbers[:index]:
                        if prev_number in rules[numbers[index]]["following"]:
                            correct_update = False
                            # Remove from previous numbers and insert right after
                            numbers.remove(prev_number)
                            numbers.insert(index + 1, prev_number)
                    for followed_number in numbers[index + 1 :]:
                        if followed_number in rules[numbers[index]]["previous"]:
                            correct_update = False
                            # Remove from following numbers and insert right before
                            numbers.remove(followed_number)
                            numbers.insert(index, followed_number)

                if not correct_update:
                    # Get the middle number of the update and add it to the sum
                    corrected_update_sum += numbers[len(numbers) // 2]

        return corrected_update_sum


# Testing and solving functions
def test_part1() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 143
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer


def test_part2() -> bool:
    filename = "./input_files/test.txt"
    expected_answer = 123
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
