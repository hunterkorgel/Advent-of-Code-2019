# Advent of Code 2019
# Day 6

input_data = []

with open('day6.txt') as file_object:
    for line in file_object:
        input_data.append(str(line.rstrip()))

# Each celestial body is unique, so we can store each body in a set. (Order doesn't matter, only identity)
# We need a function to process each line of information: 6 letters split by a parentheses.
# The left 3 letters always correspond to the object at the center of the orbit. Each orbit is one line.
# There are ~2600 direct orbits (one for each line in the file) so we need to find each body's total count of indirect orbits.

# Create a dictionary - each key is a celestial body and its value is its center of orbit
# The center of mass will not become a key of our dictionary as it orbits nothing
orbits = {}

# Function to parse an individual orbit declaration
def createDirectOrbit(orbitCode: str):
    center = orbitCode[0:3]
    orbiter = orbitCode[4:7]

    orbits[orbiter] = center

# Function to count steps for celestial body to the COM by traversing the hash table of orbit connections
def countToCOM(planet: str, x: int):
    orbiting = orbits[planet]
    while orbiting != 'COM':
        x += 1
        return countToCOM(orbiting, x)
    return x

# Function to generate list of planets visited on path to COM from any given planet
def pathToCOM(planet: str, path: list):
    orbiting = orbits[planet]

    while orbiting != 'COM':
        assert isinstance(orbiting, str)
        path.append(orbiting)
        return pathToCOM(orbiting, path)
    return path

#for orbit in input_data:
#    createOrbit(orbit)

for orbit in input_data:
    createDirectOrbit(orbit)

# total = 0
# for orbit in orbits.keys():
#     total += countToCOM(orbit, 1)

# print(total)

# Part 2: Finding the shortest number of orbit jumps to reach Santa's position of orbit
yourpath = pathToCOM('YOU', [])
santapath = pathToCOM('SAN', [])

for planet in santapath:
    if planet in yourpath:
        print(santapath.index(planet) + yourpath.index(planet))
        break
