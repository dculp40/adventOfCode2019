
class Orbit:
    def __init__(self, name, orbiters=None):
        self.name = name
        self.orbiters = orbiters if orbiters is not None else []

    def addChild(self, obj):
        self.orbiters.append(obj)

    def printOrbit(self, tabs=0):
        s = ""
        for _ in range(tabs):
            s += "\t"
        print(s + self.name)
        for subOrbit in self.orbiters:
            subOrbit.printOrbit(tabs+1)


orbitList = []
with open('orbitTestData.txt', 'r') as open_file:
    for orbit in open_file:
        orbitList.append(orbit.strip())

orbitList = [Orbit(orbitPair.split(')')[0], [Orbit(
    orbitPair.split(')')[1])]) for orbitPair in orbitList]


def getMatchingOrbits(orbitA, orbitB):
    matchingOrbits = []
    if orbitA.name == orbitB.name:
        matchingOrbits.append(orbitA)
    else:
        for subOrbit in orbitA.orbiters:
            matchingOrbits += (getMatchingOrbits(subOrbit, orbitB))
    return matchingOrbits


def mergeOrbits(orbitA, orbitB):
    for subOrbit in orbitB.orbiters:
        orbitA.addChild(subOrbit)

    # matchTest = getMatchingOrbits(orbitList[0], orbitList[2])
    # print(matchTest)
    # for orbit in matchTest:
    #     orbit.printOrbit()
# for orbit in orbitList:
#     print(matchDoesExist(orbitList[0], orbit))
#     for match in getMatchingOrbits(orbitList[0], orbit):
#         orbit.printOrbit()
#     orbit.printOrbit()


def getSize(orbit, depth):
    size = 0
    if len(orbit.orbiters) == 0:
        size = depth
    else:
        for subOrbit in orbit.orbiters:
            size += 1 + getSize(subOrbit, depth + 1)
    return size


mergeIndex = 2
while len(orbitList) > 1:
    matches = getMatchingOrbits(orbitList[0], orbitList[mergeIndex])
    # print(matches)
    if len(matches) > 0:
        mergeOrbits(matches[0], orbitList.pop(mergeIndex))
    else:
        if mergeIndex < len(orbitList):
            mergeIndex += 1
        else:
            mergeIndex = 1
orbitList[0].printOrbit()
print(getSize(orbitList[0], 0))
