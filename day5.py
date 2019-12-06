# Advent of Code 2019
# Day 5

# Use list comprehension

input_code = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 37, 34, 224, 101, -71, 224, 224, 4, 224, 1002, 223,
              8, 223, 101, 6, 224, 224, 1, 224, 223, 223, 1002, 113, 50, 224, 1001, 224, -2550, 224, 4, 224, 1002, 223,
              8, 223, 101, 2, 224, 224, 1, 223, 224, 223, 1101, 13, 50, 225, 102, 7, 187, 224, 1001, 224, -224, 224, 4,
              224, 1002, 223, 8, 223, 1001, 224, 5, 224, 1, 224, 223, 223, 1101, 79, 72, 225, 1101, 42, 42, 225, 1102,
              46, 76, 224, 101, -3496, 224, 224, 4, 224, 102, 8, 223, 223, 101, 5, 224, 224, 1, 223, 224, 223, 1102, 51,
              90, 225, 1101, 11, 91, 225, 1001, 118, 49, 224, 1001, 224, -140, 224, 4, 224, 102, 8, 223, 223, 101, 5,
              224, 224, 1, 224, 223, 223, 2, 191, 87, 224, 1001, 224, -1218, 224, 4, 224, 1002, 223, 8, 223, 101, 4,
              224, 224, 1, 224, 223, 223, 1, 217, 83, 224, 1001, 224, -124, 224, 4, 224, 1002, 223, 8, 223, 101, 5, 224,
              224, 1, 223, 224, 223, 1101, 32, 77, 225, 1101, 29, 80, 225, 101, 93, 58, 224, 1001, 224, -143, 224, 4,
              224, 102, 8, 223, 223, 1001, 224, 4, 224, 1, 223, 224, 223, 1101, 45, 69, 225, 4, 223, 99, 0, 0, 0, 677,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005,
              0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274,
              1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1,
              99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 7, 226,
              226, 224, 102, 2, 223, 223, 1005, 224, 329, 101, 1, 223, 223, 108, 677, 226, 224, 102, 2, 223, 223, 1005,
              224, 344, 1001, 223, 1, 223, 1108, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 359, 1001, 223, 1, 223, 8,
              677, 226, 224, 102, 2, 223, 223, 1006, 224, 374, 1001, 223, 1, 223, 107, 226, 226, 224, 102, 2, 223, 223,
              1006, 224, 389, 101, 1, 223, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 404, 1001, 223, 1,
              223, 108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 419, 101, 1, 223, 223, 7, 226, 677, 224, 1002, 223,
              2, 223, 1006, 224, 434, 1001, 223, 1, 223, 107, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 449, 101, 1,
              223, 223, 1108, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 464, 101, 1, 223, 223, 7, 677, 226, 224, 102,
              2, 223, 223, 1006, 224, 479, 101, 1, 223, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 494,
              101, 1, 223, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 509, 1001, 223, 1, 223, 107, 677, 677,
              224, 102, 2, 223, 223, 1006, 224, 524, 1001, 223, 1, 223, 8, 226, 226, 224, 1002, 223, 2, 223, 1005, 224,
              539, 1001, 223, 1, 223, 1007, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 554, 1001, 223, 1, 223, 1007,
              226, 226, 224, 1002, 223, 2, 223, 1005, 224, 569, 1001, 223, 1, 223, 8, 226, 677, 224, 1002, 223, 2, 223,
              1006, 224, 584, 101, 1, 223, 223, 108, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 599, 101, 1, 223, 223,
              1107, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 614, 1001, 223, 1, 223, 1107, 226, 677, 224, 102, 2,
              223, 223, 1006, 224, 629, 1001, 223, 1, 223, 1008, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 644, 101,
              1, 223, 223, 1107, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 659, 1001, 223, 1, 223, 1008, 677, 677,
              224, 102, 2, 223, 223, 1006, 224, 674, 1001, 223, 1, 223, 4, 223, 99, 226]

working_code = input_code.copy()


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


def process_opcode(code: list, index: int, input_parameter: int = None) -> int:
    # Process opcode first before trying to access full set of two or four
    opcode = code[index]
    opcode = parse_opcode(opcode)
    mode1 = opcode[1]
    mode2 = opcode[2]
    mode3 = opcode[3]
    opcode = opcode[0]

    if opcode == 99:
        result = code[0]
        #        print(result)
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
        code[first] = input_parameter
        return process_opcode(code, index + 2)
    elif opcode == 4:
        x = code[first] if mode1 == 0 else first
        print(x)
        return process_opcode(code, index + 2, (code[first] if mode1 == 0 else first))
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


def change_noun_verb(code, given_noun: int, given_verb: int):
    code[1] = given_noun
    code[2] = given_verb


# print(working_code)
print("Ready for processing.")
# print(len(working_code))

print("Processing main input....")
print("Results:")

# Processing for part 1 Air Conditioner diagnostics
#process_opcode(working_code, 0, 1)

# Processing for part 2 Thermal Radiators diagnostics
process_opcode(working_code, 0, 5)

# print(working_code)
