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

part2Coords = asteroidCoords.copy()

# returns dict where key = angle and value = array of asteroids at angle sorted by dist inc


def getAsteroidDict(station, otherAsteroids):
    asteroidDict = {}
    for asteroid in otherAsteroids:
        dx = float(asteroid[0]) - station[0]
        dy = (float(asteroid[1]) - station[1]) * -1
        # if dx == 0:
        #     if dy > 0:
        #         angle = 270
        #     else:
        #         angle = 90
        # else:
        angle = (360 - ((math.degrees(numpy.arctan2(dy, dx)) % 360) - 90)) % 360
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if angle in asteroidDict:
            asteroidDict[angle].append((distance, asteroid))
        else:
            asteroidDict[angle] = [(distance, asteroid)]

    for angle in asteroidDict:
        asteroidDict[angle] = sorted(asteroidDict[angle])
    return asteroidDict


def getBestStation(asteroidCoords):
    bestStation = None
    visibleDict = {}

    for _ in range(len(asteroidCoords)):

        potentialStation = asteroidCoords.pop(0)
        newDict = getAsteroidDict(potentialStation, asteroidCoords)

        if len(newDict) > len(visibleDict):
            bestStation = potentialStation
            visibleDict = newDict

        asteroidCoords.append(potentialStation)

    return (bestStation, visibleDict)


bestStationTup = getBestStation(asteroidCoords)
# print(bestStationTup[0], len(bestStationTup[1]))

# station = (8, 3)
# part2Coords.remove(station)
# asteroidDict = getAsteroidDict(station, part2Coords)

station = bestStationTup[0]
asteroidDict = bestStationTup[1]
# print(sorted(asteroidDict))
# print(asteroidDict[0.0])
blastLog = []

while len(asteroidDict) > 0:
    for angle in sorted(asteroidDict):
        if len(asteroidDict[angle]) > 0:
            blastLog.append(asteroidDict[angle].pop(0)[1])
        else:
            asteroidDict.pop(angle)

print(blastLog[199])


def getVisibleAsteroidMeasurements(station, otherAsteroids):
    visibleAsteroidMeasurements = otherAsteroids.copy()
    j = 0
    while j < len(visibleAsteroidMeasurements) - 1:
        # asteroidVisible = True
        for measurement in visibleAsteroidMeasurements[j+1:]:
            if visibleAsteroidMeasurements[j][0] == measurement[0]:
                visibleAsteroidMeasurements.remove(measurement)
        j += 1
    return visibleAsteroidMeasurements


# otherAsteroids = getOtherAsteroidMeasurementsSorted((29, 28), asteroidCoords)

# while len(visibleAsteroids) > 0 and nextangle > thisangle:
#     startingAngle = 0

#     target = visibleAsteroids.pop(0)
#     if something behind:
#         replace target with something
#     else
#     remove target
#     shootAsteroid
#     add asteroids with


# mostVisible = 0
# bestStation = None


# print(bestStation)
# print(mostVisible)
