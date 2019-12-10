# Advent of Code 2019
# Day 7

from itertools import permutations

input_code = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 42, 67, 88, 105, 114, 195, 276, 357, 438, 99999, 3, 9, 101, 4, 9,
              9, 102, 3, 9, 9, 1001, 9, 2, 9, 102, 4, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 4, 9, 102, 4, 9, 9, 101, 2, 9, 9,
              1002, 9, 5, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 1001, 9, 4, 9, 1002, 9, 4, 9, 101, 2, 9, 9, 1002, 9, 2, 9,
              4, 9, 99, 3, 9, 101, 4, 9, 9, 102, 3, 9, 9, 1001, 9, 5, 9, 4, 9, 99, 3, 9, 102, 5, 9, 9, 4, 9, 99, 3, 9,
              102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9,
              102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9,
              102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3,
              9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9,
              1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3,
              9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3,
              9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3,
              9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4,
              9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4,
              9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4,
              9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9,
              4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9,
              4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99]

working_code = input_code.copy()

test_code1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
test_code2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]
test_code3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

test_set1 = [4,3,2,1,0]
test_set2 = [0,1,2,3,4]
test_set3 = [1,0,4,3,2]

# We will reuse our existing "intcode" computer for this day's assignment
def parse_opcode(opcode: int):
    opcode = str(opcode)
    mode1 = 0
    mode2 = 0
    mode3 = 0

    if len(opcode) > 1:
        instruction = int(opcode[-1]) + (int((opcode[-2])) * 10)
    else:
        instruction = int(opcode[-1])

    if len(opcode) > 2:
        mode1 = opcode[-3]
        if len(opcode) > 3:
            mode2 = opcode[-4]
            if len(opcode) > 4:
                mode3 = opcode[-5]

    return [instruction, int(mode1), int(mode2), int(mode3)]


stored_value = None
output_value = None


def process_opcode(code: list, index: int, input_parameter: int = None):
    # Process opcode first before trying to access full set of two or four
    opcode = code[index]
    opcode = parse_opcode(opcode)
    mode1 = opcode[1]
    mode2 = opcode[2]
    mode3 = opcode[3]
    opcode = opcode[0]

    if opcode == 99:
        result = code[0]
        # print(result)
        return result

    # Process scope of 3 other values for later handling
    first = code[index + 1]
    second = code[index + 2]
    third = code[index + 3]

    # Main recursive loop to handle and process code sequence
    if opcode == 1:
        code[third] = (code[first] if mode1 == 0 else first) + (code[second] if mode2 == 0 else second)
        return process_opcode(code, index + 4)
    elif opcode == 2:
        code[third] = (code[first] if mode1 == 0 else first) * (code[second] if mode2 == 0 else second)
        return process_opcode(code, index + 4)
    elif opcode == 3:
        if input_parameter == None:
            global stored_value
            code[first] = stored_value
        else:
            code[first] = input_parameter
        return process_opcode(code, index + 2)
    elif opcode == 4:
        global output_value
        x = code[first] if mode1 == 0 else first
        output_value = x
        return process_opcode(code, index + 2, x)
    elif opcode == 5:
        if (code[first] if mode1 == 0 else first) != 0:
            return process_opcode(code, (code[second] if mode2 == 0 else second))
        else:
            return process_opcode(code, index + 3)
    elif opcode == 6:
        if (code[first] if mode1 == 0 else first) == 0:
            return process_opcode(code, (code[second] if mode2 == 0 else second))
        else:
            return process_opcode(code, index + 3)
    elif opcode == 7:
        if (code[first] if mode1 == 0 else first) < (code[second] if mode2 == 0 else second):
            code[third] = 1
        else:
            code[third] = 0
        return process_opcode(code, index + 4)
    elif opcode == 8:
        if (code[first] if mode1 == 0 else first) == (code[second] if mode2 == 0 else second):
            code[third] = 1
        else:
            code[third] = 0
        return process_opcode(code, index + 4)
    else:
        print("Opcode error: must be 99, 1, 2, 3, or 4.")
        print("Opcode: " + str(opcode))
        # return result


# Function that handles a single amplifier's operation
def run_amplifier(code: list, phase_code: int, input_signal: int):
    global stored_value
    stored_value = input_signal
    process_opcode(code, 0, phase_code)


# Function that runs the set of amplifiers according to the configured order of phase codes
def run_amp_set(code: list, phase_code_set: list) -> int:
    global output_value
    output_value = 0
    for phase_code in phase_code_set:
        run_amplifier(code, phase_code, output_value)
    return output_value

#run_amp_set(test_code1, test_set1)
#run_amp_set(test_code2, test_set2)
#run_amp_set(test_code3, test_set3)

li = [0,1,2,3,4]
allofthem = permutations(li)

biggest = 0
combo = []
for x in allofthem:
    result = run_amp_set(working_code, x)
    if result > biggest:
        biggest = result
        combo = x

print(biggest)
print(combo)