import math


class Moon:
    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]

    def applyGravity(self, otherMoon):
        for i in range(3):
            if otherMoon.position[i] > self.position[i]:
                self.velocity[i] += 1
            if otherMoon.position[i] < self.position[i]:
                self.velocity[i] -= 1

    def applyVelocity(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    def getEnergy(self):
        potential = 0
        kinetic = 0
        for i in range(3):
            potential += abs(self.position[i])
            kinetic += abs(self.velocity[i])
        return potential * kinetic


# moons = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
moons = [[-9, 10, -1], [-14, -8, 14], [1, 5, 6], [-19, 7, 8]]
moons = [Moon(position) for position in moons]

steps = 1000

for i in range(steps):
    for _ in range(len(moons)):
        currMoon = moons.pop(0)
        for otherMoon in moons:
            currMoon.applyGravity(otherMoon)
        moons.append(currMoon)
    for moon in moons:
        moon.applyVelocity()
        # print(moon.position, moon.velocity)
    # print('\n')

totalEnergy = 0
for moon in moons:
    print(moon.position, moon.velocity)
    totalEnergy += moon.getEnergy()
print(totalEnergy)
