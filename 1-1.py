import math

# 1-1


def getFuel(mass):
    return math.floor(mass / 3) - 2

# 1-2


def getTotalFuel(mass):
    extraFuel = math.floor(mass / 3) - 2
    if extraFuel > 0:
        return extraFuel + getTotalFuel(extraFuel)
    else:
        return 0


total_fuel = 0

with open('modules.txt', 'r') as open_file:
    for module in open_file:
        total_fuel += getTotalFuel(int(module))

print(total_fuel)
