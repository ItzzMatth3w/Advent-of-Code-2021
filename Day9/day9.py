# Day 9 - Smoke Basin

# Input Handling
with open('Day9/day9.in') as fin:
    data = [[int(i) for i in line] for line in fin.read().strip().split('\n')] 

# Part 1 - Finding the total risk level
def part1():
    totalRisk = 0

    # Disect the map
    rows = len(data)
    cols = len(data[0])

    # Used for checking surrounding positions
    shifts = [(0,1),(0, -1),(-1, 0),(1, 0)]

    # Travel to every position on the map
    for row in range(rows):
        for col in range(cols):
            
            # Check every location
            lowPointFound = True                   # Stop once we find the lowpoint
            for shift in shifts:
                rowShift = row + shift[0]
                colShift = col + shift[1]

                # Avoiding any indexing errors
                if ((0 <= rowShift and rowShift < rows) and (0 <= colShift and colShift < cols)):

                    # Check if there is a low point
                    if data[row][col] >= data[rowShift][colShift]:
                        lowPointFound = True
                        break
                
            if lowPointFound:
                totalRisk += data[row][col] + 1 

    return totalRisk


# Part 2 - 
def part2():
    

    pass


# Answers:
print(f'Answer to part 1: {part1()}')
print(f'Answer to part 2: {part2()}')
