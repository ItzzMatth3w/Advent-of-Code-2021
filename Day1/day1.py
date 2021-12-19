
# Getting data
with open("Day1/day1.in") as fin:
    data = [int(i) for i in fin.read().strip().split("\n")]

# print(data)

def part1():
    result = [firstNum < secondNum for firstNum, secondNum in zip(data, data[1:])]
    
    return sum(result)


def part2():
    allSums = [sum(someTuple) for someTuple in zip(data, data[1:], data[2:])]
    result = [firstSum < secondSum for firstSum, secondSum in zip(allSums, allSums[1:])]

    return sum(result)

print("Answer to part one: ", part1())
print("Answer to part two: ", part2())
