import math

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

mostVisible = 0
bestStation = None
for i in range(len(asteroidCoords)):
    asteroidMeasurements = []
    potentialStation = asteroidCoords.pop(0)
    for asteroid in asteroidCoords:
        dx = asteroid[0] - potentialStation[0]
        dy = asteroid[1] - potentialStation[1]
        if dx == 0:
            if dy > 0:
                slope = "-inf"
            else:
                slope = "+inf"
        elif dy == 0:
            if dx > 0:
                slope = "+zero"
            else:
                slope = "-zero"
        else:
            slope = dy/dx
        distance = math.sqrt(dx ** 2 + dy ** 2)
        asteroidMeasurements.append((slope, distance))

    visibleAsteroidMeasurements = []
    asteroidMeasurements = sorted(asteroidMeasurements, key=lambda x: x[1])
    j = 0
    while j < len(asteroidMeasurements) - 1:
        #asteroidVisible = True
        for measurement in asteroidMeasurements[j+1:]:
            if asteroidMeasurements[j][0] == measurement[0]:
                asteroidMeasurements.remove(measurement)
        j += 1
    print(potentialStation, len(asteroidMeasurements))
    if len(asteroidMeasurements) > mostVisible:
        bestStation = potentialStation
        mostVisible = len(asteroidMeasurements)

    asteroidCoords.append(potentialStation)

print(bestStation)
print(mostVisible)
