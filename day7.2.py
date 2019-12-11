# Advent of Code 2019
# Day 7, Part 2
# Now with a complete restructuring of the IntCode computer to enable better solution design

import intcode as ic
from itertools import permutations, cycle

input_memory = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 42, 67, 88, 105, 114, 195, 276, 357, 438, 99999, 3, 9, 101, 4,
                9, 9, 102, 3, 9, 9, 1001, 9, 2, 9, 102, 4, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 4, 9, 102, 4, 9, 9, 101, 2, 9,
                9, 1002, 9, 5, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 1001, 9, 4, 9, 1002, 9, 4, 9, 101, 2, 9, 9, 1002, 9, 2,
                9, 4, 9, 99, 3, 9, 101, 4, 9, 9, 102, 3, 9, 9, 1001, 9, 5, 9, 4, 9, 99, 3, 9, 102, 5, 9, 9, 4, 9, 99, 3,
                9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3,
                9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9,
                3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9,
                4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9,
                4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2,
                9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002,
                9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102,
                2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3,
                9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9,
                3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4,
                9, 3, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2,
                9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9,
                1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99]

working_memory = input_memory.copy()


def run_amps_feedback(memory, preset: list):
    amplifierA = ic.IntCode('A', memory, [preset[0]])
    amplifierB = ic.IntCode('B', memory, [preset[1]])
    amplifierC = ic.IntCode('C', memory, [preset[2]])
    amplifierD = ic.IntCode('D', memory, [preset[3]])
    amplifierE = ic.IntCode('E', memory, [preset[4]])

    amp_list = [amplifierA, amplifierB, amplifierC, amplifierD, amplifierE]

    # Initialize all 5 amplifiers by feeding them their phase codes and jumping them
    amp_list[0].executeIntCode()

    amp_list[1].executeIntCode()

    amp_list[2].executeIntCode()

    amp_list[3].executeIntCode()

    amp_list[4].executeIntCode()

    amplifiers_cycle = cycle(amp_list)

    amplitude = 0

    # Primary amplification loop
    for amp in amplifiers_cycle:
        if amp.mem[amp.pointerAddress] == 99:
            break
        amp.writeRam(amplitude)
        amp.executeIntCode()
        amplitude = amp.readRam()

    return amplitude


test1 = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
         27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
test2 = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
         -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
         53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]

# run_amps_feedback(test1, [9,8,7,6,5])
# run_amps_feedback(test2, [9,7,8,5,6])

li = [5, 6, 7, 8, 9]
allofthem = permutations(li)

biggest = 0
combo = []
for x in allofthem:
    result = run_amps_feedback(working_memory.copy(), x)
    if result > biggest:
        biggest = result
        combo = x

print(biggest)
print(combo)
