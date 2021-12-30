# Day 7 - The Treachery of Whales

# Imports
from statistics import median

# Input handling
with open('Day7/day7.in') as fin:
    data = [int(i) for i in fin.read().strip().split(',')]

# Part 1:
def part1():
    med = int(median(data))                 # Median is the best as it is the closest to all values
    fuelSpent = 0                                
    
    for horizontal in data:                 # Takes every crab position             
        fuelSpent += abs(horizontal - med)           # Find the POSITIVE difference, which is fuelSpent

    return fuelSpent


# Calculate fuelSpent for part 2
def triangular_cost(steps):
    return (steps * (steps + 1))//2


# Part 2:
def part2():
    minFuel = 1 << 100                              # Assign a really big number
    max_pos = max(data)                             # Get biggest possible position
    min_pos = min(data)                             # Get smallest possible position
    
    # Go through every possible position  
    for pos in range(min_pos, max_pos):                 
        
        # Calculate total fuel at that position
        fuel = 0 
        for crab in data:
            cost = triangular_cost(abs(crab-pos))
            fuel += cost
        
        # Keep only the smallest fuel
        minFuel = min(minFuel, fuel)
    
    return minFuel


# Answers
print(f'Answer to part 1: {part1()}')
print(f'Answer to part 2: {part2()}')