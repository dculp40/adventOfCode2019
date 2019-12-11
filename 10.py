import math
import numpy

mapArr = []

with open('asteroidMap.txt', 'r') as open_file:
    for line in open_file:
        mapArr.append(line)


asteroidCoords = []
for row in range(len(mapArr)):
    for column in range(len(mapArr[row])):
        if mapArr[row][column] == '#':
            asteroidCoords.append((column, row))

# print(asteroidCoords)

asteroidCoords.remove((29, 28))


def getOtherAsteroidMeasurementsSorted(station, otherAsteroids):
    asteroidMeasurements = []
    for asteroid in otherAsteroids:
        dx = float(asteroid[0]) - station[0]
        dy = float(asteroid[1]) - station[1]
        if dx == 0:
            if dy > 0:
                angle = 270
            else:
                angle = 90
        # elif dy == 0:
        #     if dx > 0:
        #         angle = "+zero"
        #     else:
        #         angle = "-zero"
        else:
            angle = math.degrees(numpy.arctan2(dy, dx))
        distance = math.sqrt(dx ** 2 + dy ** 2)
        asteroidMeasurements.append((angle, distance))
    return sorted(asteroidMeasurements, key=lambda x: x[1])


def getVisibleAsteroidMeasurements(station, otherAsteroids):
    visibleAsteroidMeasurements = otherAsteroids.copy()
    j = 0
    while j < len(visibleAsteroidMeasurements) - 1:
        #asteroidVisible = True
        for measurement in visibleAsteroidMeasurements[j+1:]:
            if visibleAsteroidMeasurements[j][0] == measurement[0]:
                visibleAsteroidMeasurements.remove(measurement)
        j += 1
    return visibleAsteroidMeasurements


mostVisible = 0
bestStation = None
for i in range(len(asteroidCoords)):

    potentialStation = asteroidCoords.pop(0)
    asteroidMeasurements = getOtherAsteroidMeasurementsSorted(
        potentialStation, asteroidCoords)

    print(potentialStation, len(asteroidMeasurements))
    if len(asteroidMeasurements) > mostVisible:
        bestStation = potentialStation
        mostVisible = len(asteroidMeasurements)

    asteroidCoords.append(potentialStation)

print(bestStation)
print(mostVisible)
