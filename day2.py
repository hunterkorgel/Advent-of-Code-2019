# Advent of Code 2019
# Day 2

# Use list comprehension

input_code = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 6, 23, 2, 6, 23, 27, 2, 27, 9, 31, 1,
              5, 31, 35, 1, 35, 10, 39, 2, 39, 9, 43, 1, 5, 43, 47, 2, 47, 10, 51, 1, 51, 6, 55, 1, 5, 55, 59, 2, 6, 59,
              63, 2, 63, 6, 67, 1, 5, 67, 71, 1, 71, 9, 75, 2, 75, 10, 79, 1, 79, 5, 83, 1, 10, 83, 87, 1, 5, 87, 91, 2,
              13, 91, 95, 1, 95, 10, 99, 2, 99, 13, 103, 1, 103, 5, 107, 1, 107, 13, 111, 2, 111, 9, 115, 1, 6, 115,
              119, 2, 119, 6, 123, 1, 123, 6, 127, 1, 127, 9, 131, 1, 6, 131, 135, 1, 135, 2, 139, 1, 139, 10, 0, 99, 2,
              0, 14, 0]

working_code = input_code.copy()


def process_opcode(code, index):
    # Process opcode first before trying to access full set of four
    opcode = code[index]
    if opcode == 99:
        result = code[0]
        #        print(result)
        return result

    # Process scope of 3 other values for later handling
    first = code[index + 1]
    second = code[index + 2]
    target = code[index + 3]

    # Debug step
    # print(code[index:(index+4)])

    # Main recursive loop to handle and process code sequence
    if opcode == 1:
        code[target] = (code[first]) + (code[second])
        return process_opcode(code, index + 4)
    elif opcode == 2:
        code[target] = (code[first]) * (code[second])
        return process_opcode(code, index + 4)
    else:
        print("Opcode error: must be 99, 1, or 2.")
        # return result


def change_noun_verb(code, noun: int, verb: int):
    code[1] = noun
    code[2] = verb


# Solution from Part 1:

# print("Restoring main input to \"1202 program alarm\" state.")
# change_noun_verb(input_code, 12, 2)
# print(input_code)
# print("Ready for processing.")

# print("Processing main input....")
# print("Results:")
# process_opcode(input_code, 0)
# print(input_code)

# Begin Part 2:
another = True

for noun in range(0, 100):
    if not another:
        exit()
    for verb in range(0, 100):
        if not another:
            exit()
        working_code = input_code.copy()
        #        print(working_code)
        change_noun_verb(working_code, noun, verb)
        #        print(working_code)
        #        print(noun)
        #        print(verb)
        x = process_opcode(working_code, 0)
        #        print(x)
        if x == 19690720:
            print(noun)
            print(verb)
            another = False
            exit()
