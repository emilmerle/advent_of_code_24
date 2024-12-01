from pathlib import Path

def algorithm_1(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as f:
        left_list = []
        right_list = []
        for line in f:
            index = line.index(" ")
            # first number is before the first space
            # second number is after the third space
            left_list.append(int(line[:index]))
            right_list.append(int(line[index+2:]))
        left_list = sorted(left_list)
        right_list = sorted(right_list)
        # sum up the differences of every number pair
        answer = sum([abs(a - b) for a,b in zip(left_list, right_list)])
        return answer
    

def algorithm_2(input_filename: str) -> int:
    path = Path(input_filename)
    with open(path, "r") as f:
        left_list = []
        right_list = []
        for line in f:
            index = line.index(" ")
            # first number is before the first space
            # second number is after the third space
            left_list.append(int(line[:index]))
            right_list.append(int(line[index+2:]))
        left_list = sorted(left_list)
        right_list = sorted(right_list)
        # count occurences of left item in right list and multiply the number with the number of occurences
        answer = sum([item * right_list.count(item) for item in left_list])
        return answer


def test_part1():
    filename = "./input_files/test.txt"
    expected_answer = 11
    algorithm_answer = algorithm_1(filename)
    return expected_answer == algorithm_answer

def test_part2():
    filename = "./input_files/test.txt"
    expected_answer = 31
    algorithm_answer = algorithm_2(filename)
    return expected_answer == algorithm_answer

def solve_part1():
    filename = "./input_files/puzzle.txt"
    algorithm_answer = algorithm_1(filename)
    return algorithm_answer

def solve_part2():
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