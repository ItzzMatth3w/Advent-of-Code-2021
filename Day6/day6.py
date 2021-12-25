
# Input Handling
with open('Day6/day6.in') as fin:
    allFish = [int(i) for i in fin.read().strip().split(',')]


# Part 1:
def part1():
    DAYS = 80

    # Run simulation for 80 days
    while DAYS > 0:
        
        # Check for fishes that have to reproduce
        for fish in range(0, len(allFish)):
            if allFish[fish] == 0:
                allFish[fish] = 7
                allFish.append(9)
        
        # Decrease all fishes reproduction days by 1
        for fish in range(0, len(allFish)):
            allFish[fish] -= 1

        DAYS -= 1

    return len(allFish)


# Part 2:
def part2():
    pass


print("Answer to part 1: ", part1())
print("Answer to part 2: ", part2())