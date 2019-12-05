# Advent of Code 2019
# Day 4

# Create a list of all starting values and remove invalid passwords until only valid options remain
list = []
#print(len(list))

# A set of functions to remove invalid passwords from the list
# Evaluates a 6-digit number and returns True if it contains an adjacent repeated digit
# ****** modified in part two to return True only if at least one adjacent repeated pair isn't part of a larger repetition
def hasAdjacentRepeat(number):
    number = str(number)
    last_digit = None
    two_digits_ago = None
    truth = False
    index = 0
    for digit in number:
        if digit == last_digit and not digit == two_digits_ago:
            if index < len(number) - 1:
                if digit != number[index + 1]:
                    return True
            else:
                return True
        two_digits_ago = last_digit
        last_digit = digit
        index += 1
    return False

#print(hasAdjacentRepeat(123456))
#print(hasAdjacentRepeat(123455))
#print(hasAdjacentRepeat(111224))

# Evaluates a number and returns True if it contains a decreasing digit
def hasDecreasingDigit(number):
    number = str(number)
    last_digit = None
    for digit in number:
        if digit < last_digit:
            return True
        last_digit = digit
    return False

#print(hasDecreasingDigit(123456))
#print(hasDecreasingDigit(123455))

# Apply both eliminating functions in a single operation to the list of possible passwords
for password in range(372037, 905158):
    if hasAdjacentRepeat(password) and not hasDecreasingDigit(password):
        list.append(password)
    else:
        continue

#print(hasAdjacentRepeat(112233) and not hasDecreasingDigit(112233))
#print(hasAdjacentRepeat(123444) and not hasDecreasingDigit(123444))
#print(hasAdjacentRepeat(111122) and not hasDecreasingDigit(111122))
#print(hasAdjacentRepeat(112222) and not hasDecreasingDigit(112222))

# Display the results
print(len(list))
