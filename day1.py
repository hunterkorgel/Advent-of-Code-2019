### Advent of Code
### Day 1

fuel_total = 0

additional_fuel = 0

filename = 'day1input.txt'

def fuelcalc(number):
    answer = ((number / 3)//1) - 2
    return answer
    
def fuelsum(number):
    total = 0
    number = int(number)
    while fuelcalc(number) > 0:
        total += fuelcalc(number)
        number = fuelcalc(number)
    return total

with open(filename) as file_object:
    for line in file_object:
        mass = int(line)
        fuel = fuelsum(mass)
        fuel_total += fuel
        
print(fuel_total)



#print("Total fuel = " + str(fuel_total) + ".")
additional_fuel = ((fuel_total / 3)//1) - 2


while additional_fuel > 0:
#    print("Adding " + str(additional_fuel) + " fuel.")
    fuel_total += additional_fuel
    additional_fuel = ((additional_fuel / 3)//1) - 2

print(fuel_total)
