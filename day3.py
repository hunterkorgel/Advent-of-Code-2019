# Advent of Code 2019
# Day 3

# Use tuples for coordinates
# List of tuples for each wire?

# Then we can identify tuples that match across dictionaries as intersections
# Central port starts at (0, 0)

# Manhattan distance to each intersection is the sum of the tuples components

with open('day3input.txt') as file_object:
    lines = file_object.readlines()
    instructions1 = lines[0].rstrip().split(",")
    instructions2 = lines[1].rstrip().split(",")

#print(instructions1)
#print(instructions2)

# Creating the coordinate pair class
class Coordinate():
    """A data type to store coordinate information."""
    
    def __init__(self, x, y):
        """Initialize the x and y values."""
        self.x = x
        self.y = y

    def __eq__(self, coordinate2):
        if self.x == coordinate2.x and self.y == coordinate2.y:
            return True
        else:
            return False

    def __hash__(self):
        """Clarify hashing method."""
        return hash((self.x, self.y))

    def get_distance(self):
        distance = abs(self.x) + abs(self.y)
        return distance
    
    def display(self):
        string = str(self.x) + ", " + str(self.y)
        return string
        
origin = Coordinate(0, 0)

# Instantiating the list for each wire
wire1 = [origin]
wire2 = [origin]
        
# Defining a function to handle each instruction. Draws a line segment
def segment(wire, instruction):
    direction = instruction[:1]
    distance = int(instruction[1:])
    
    # Retrieve the starting point coordinate
    start = wire[-1]
    
    # For the given direction track each coordinate
    # touched in the wire's path list
    if direction == 'R':
        xcursor = start.x
        ycursor = start.y

        for step in range(0,distance):
            wire.append(Coordinate(xcursor + 1, ycursor))
            xcursor += 1
            
    elif direction == 'U':
        xcursor = start.x
        ycursor = start.y
        
        for step in range(0,distance):
            wire.append(Coordinate(xcursor, ycursor + 1))
            ycursor += 1

    elif direction == 'L':
        xcursor = start.x
        ycursor = start.y
        
        for step in range(0,distance):
            wire.append(Coordinate(xcursor - 1, ycursor))
            xcursor -= 1

    elif direction == 'D':
        xcursor = start.x
        ycursor = start.y
        
        for step in range(0,distance):
            wire.append(Coordinate(xcursor, ycursor - 1))
            ycursor -= 1
    
    else:
        print("Error!")
        return 0

#segment(wire1, "L75")
#segment(wire1, "U30")

# Drawing each wire based on each set of instructions
for instruction in instructions1:
    segment(wire1, instruction)
    
for instruction in instructions2:
    segment(wire2, instruction)

# Print the head of each wire for debugging purposes
#print(wire1[-1].display())
#print(wire2[-1].display())

#print(len(wire1))
#print(len(wire2))

#print(len(set(wire1)))
#print(len(set(wire2)))

# Find all intersections; where the wires share a coordinate with each other
intersections = set(wire1).intersection(set(wire2))
#print(len(intersections))

# Find all Manhattan distances to intersections
#for x in intersections:
#    print(x.get_distance())

totals = []

for x in intersections:
#    print(x.display())
    steps1 = wire1.index(x)
    steps2 = wire2.index(x)
    total = steps1 + steps2
#    print(total)
    totals.append(total)
#    print(len(totals))

totals.remove(0)
smallest = min(totals)
print(smallest)