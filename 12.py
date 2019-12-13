import sys


class Moon:
    def __init__(self, position):
        self.position = position
        self.start = position
        self.velocity = [0, 0, 0]
        self.positionLog = []
        self.velocityLog = []
        # self.beenHereBefore = False

    def applyGravity(self, otherMoon):
        for i in range(3):
            if otherMoon.position[i] > self.position[i]:
                self.velocity[i] += 1
            if otherMoon.position[i] < self.position[i]:
                self.velocity[i] -= 1

    def applyVelocity(self):
        for i in range(3):
            self.position[i] += self.velocity[i]
        log = self.position.copy() + self.velocity.copy()
        if log in self.log:
            print(self.start, self.position, len(self.log))
        else:
            self.log.append(log)
        # logInt = vectorToInt(
        #     self.position.copy()+self.velocity.copy())
        # if logInt not in self.log:
        #     self.beenHereBefore = False
        #     self.log.append(logInt)
        # else:
        #     self.beenHereBefore = True

    def getEnergy(self):
        potential = 0
        kinetic = 0
        for i in range(3):
            potential += abs(self.position[i])
            kinetic += abs(self.velocity[i])
        return potential * kinetic


# moons = [[-1, 0, 2], [2, -10, -7], [4, -8, 8],[3, 5, -1]]  # 2772 steps to repeat
moons = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]  # 4686774924
# moons = [[-9, 10, -1], [-14, -8, 14], [1, 5, 6], [-19, 7, 8]]
moons = [Moon(position) for position in moons]

steps = 0
combinedPVLog = []


def getCombinedPVHash(moons):
    h = []
    for moon in moons:
        h.append(moon.position.copy() + moon.velocity.copy())
    return hash(str(h))


def progressBar(value, endvalue, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(
        arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()


historyRepeats = False
# for i in range(steps):
while not historyRepeats:
    log = getCombinedPVHash(moons)
    combinedPVLog.append(log)

    # individualRepeats = True
    for _ in range(len(moons)):
        currMoon = moons.pop(0)
        for otherMoon in moons:
            currMoon.applyGravity(otherMoon)
        moons.append(currMoon)
    for moon in moons:
        moon.applyVelocity()
        # individualRepeats = individualRepeats and moon.beenHereBefore
    steps += 1
    # print(moon.position, moon.velocity)
    # print('\n')
    if getCombinedPVHash(moons) in combinedPVLog:
        print(steps, log)
        historyRepeats = True
    #progressBar(steps, 4686774924)

print(steps)

# totalEnergy = 0
# for moon in moons:
#     print(moon.position, moon.velocity)
#     totalEnergy += moon.getEnergy()
# print(totalEnergy)
