
class Orbit:
    def __init__(self, name, orbiters=[]):
        self.name = name
        self.orbiters = orbiters

    def addChild(self, object):
        self.orbiters.append(object)

    def printOrbit(self, tabs=0):
        s = ""
        for _ in range(tabs):
            s += "\t"
        print(s + self.name)
        for subOrbit in self.orbiters:
            subOrbit.printOrbit(tabs+1)


orbitList = []
with open('testData.txt', 'r') as open_file:
    for orbit in open_file:
        orbitList.append(orbit.strip())

firstOrbit = orbitList.pop(0).split(')')
rootOrbit = Orbit(firstOrbit[0], [Orbit(firstOrbit[1])])
rootOrbit.printOrbit()


def hasMatchingOrbit(orbit, targetName):
    match = False
    if(orbit.name == targetName):
        match = True
    else:
        for subOrbit in orbit.orbiters:
            match = match | hasMatchingOrbit(subOrbit, targetName)
    return match


def getMatchingOrtbit(orbit, targetName):
    match = []
    if(orbit.name == targetName):
        match.append(orbit)
        return orbit
    else:
        for subOrbit in orbit.orbiters:
            match.append(getMatchingOrtbit(subOrbit, targetName))
    return match


def mergeOrbits(orbit, targetName, newOrbit):
    print("adding: " + newOrbit.name)
    if(orbit.name == targetName):
        orbit.addChild(newOrbit)
    else:
        for subOrbit in orbit.orbiters:
            mergeOrbits(subOrbit, targetName, newOrbit)


#print(hasMatchingOrbit(rootOrbit, 'elf'))

orbitToMergeIndex = 0
while len(orbitList) > 0:
    newOrbitString = orbitList[orbitToMergeIndex]
    centerName = newOrbitString.strip().split(')')[0]
    orbiterName = newOrbitString.strip().split(')')[1]
    print(orbiterName)
    if hasMatchingOrbit(rootOrbit, centerName):
        getMatchingOrtbit(rootOrbit, centerName)[
            0].addChild(Orbit(orbiterName))
        print(orbitList)
        orbitList.remove(newOrbitString)
    else:
        orbitToMergeIndex += 1

    # for orbit in orbitList:
    #     print(orbit)
    #     centerName = orbit.strip().split(')')[0]
    #     orbiterName = orbit.strip().split(')')[1]
    #     if orbiterName == rootOrbit.name:
    #         rootOrbit = Orbit(centerName, [rootOrbit])
    #     if hasMatchingOrbit(rootOrbit, centerName):
    #         findMatchAddChild(rootOrbit, centerName, Orbit(orbiterName))
    #         orbitList.remove(orbit)
        # rootOrbit.printOrbit()
    # print(orbitList)


#         addOrbiter
#     else:

#     print(orbit.name)

# # print(orbit.strip().split(')')[0])
#         centerName = orbit.strip().split(')')[0]
#         orbiterName = orbit.strip().split(')')[1]

#         orbitList.append(Node(orbiterName))
