# Day 2: Dive! 


# Get data from file
with open("day2.in") as fin:
    data = [i for i in fin.read().strip().split("\n")]

# print(data)

# Part 1
def part1():
    horizontal = 0
    depth = 0

    for instruction in data:
        command = instruction[:-2]
        move = int(instruction[-1])

        if command == 'forward':
            horizontal += move
        elif command == 'down':
            depth += move
        elif command == 'up':
            depth -= move

    return horizontal * depth


# Part 2
def part2():
    horizontal = 0
    depth = 0
    aim = 0

    for instruction in data:
        command = instruction[:-2]
        move = int(instruction[-1])

        if command == 'forward':
            horizontal += move
            depth += aim * move
        elif command == 'down':
            aim += move
        elif command == 'up':
            aim -= move

    return horizontal * depth

print("Answer to part 1: ", part1())
print("Answer to part 2: ", part2())
