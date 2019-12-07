
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
with open('orbitRealData.txt', 'r') as open_file:
    for orbit in open_file:
        orbitList.append(orbit.strip())

orbitList = [Orbit(orbitPair.split(')')[0], [Orbit(
    orbitPair.split(')')[1])]) for orbitPair in orbitList]


def getMatchingOrbits(orbitToSeek, orbitToCrawl):
    matchingOrbits = []
    if orbitToCrawl.name == orbitToSeek.name:
        matchingOrbits.append(orbitToCrawl)
    else:
        for subOrbit in orbitToCrawl.orbiters:
            matchingOrbits += (getMatchingOrbits(orbitToSeek, subOrbit))
    return matchingOrbits


def mergeOrbits(orbitToKeep, orbitToInsert):
    for subOrbit in orbitToInsert.orbiters:
        orbitToKeep.addChild(subOrbit)

    # matchTest = getMatchingOrbits(orbitList[0], orbitList[2])
    # print(matchTest)
    # for orbit in matchTest:
    #     orbit.printOrbit()
# for orbit in orbitList:
#     print(matchDoesExist(orbitList[0], orbit))
#     for match in getMatchingOrbits(orbitList[0], orbit):
#         orbit.printOrbit()
#     orbit.printOrbit()


def getIterativeDepth(orbit, depth):
    currDepth = depth
    if len(orbit.orbiters) == 0:
        return currDepth
    else:
        for subOrbit in orbit.orbiters:
            currDepth += getIterativeDepth(subOrbit, depth + 1)
    return currDepth


# def orbitsCanMerge(orbitA, orbitB):
#     return len(getMatchingOrbits(orbitA, orbitB) + getMatchingOrbits(orbitB, orbitA))


# mergeIndex = 1
# while len(orbitList) > 1:
#     print(len(orbitList), mergeIndex)
#     matches = getMatchingOrbits(orbitList[0], orbitList[mergeIndex])
#     # print(matches)
#     if len(matches) > 1:
#         print("ERROR")
#     if len(matches) > 0:
#         mergeOrbits(matches[0], orbitList.pop(mergeIndex))
#         print(len(orbitList))
#     else:
#         if mergeIndex < len(orbitList) - 1:
#             mergeIndex += 1
#         else:
#             mergeIndex = 1
#     orbitList[0].printOrbit()
# print(getIterativeDepth(orbitList[0], 0))

# currOrbitIndex = 0
# searchOrbitIndex = 0
# while len(orbitList) > 1:
#     currOrbit = orbitList[currOrbitIndex]
#     while searchOrbitIndex < len(orbitList):
#         if currOrbitIndex != searchOrbitIndex:
#             searchOrbit = orbitList[searchOrbitIndex]
#             matches = getMatchingOrbits(currOrbit, searchOrbit)
#             if len(matches) > 0:
#                 mergeOrbits(searchOrbit, orbitList.pop(currOrbitIndex))
#                 break
#         searchOrbitIndex += 1


while len(orbitList) > 1:
    orbitToMerge = orbitList.pop(0)
    targetOrbit = []
    searchIndex = 0
    while searchIndex < len(orbitList):
        targetOrbit += getMatchingOrbits(orbitToMerge, orbitList[searchIndex])
        searchIndex += 1
    if len(targetOrbit) > 0:
        mergeOrbits(targetOrbit[0], orbitToMerge)
    else:
        orbitList.append(orbitToMerge)

orbitList[0].printOrbit()
print(getIterativeDepth(orbitList[0], 0))
