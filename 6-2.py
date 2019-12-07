
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


def getIterativeDepth(orbit, depth):
    currDepth = depth
    if len(orbit.orbiters) == 0:
        return currDepth
    else:
        for subOrbit in orbit.orbiters:
            currDepth += getIterativeDepth(subOrbit, depth + 1)
    return currDepth


def path(root, targetOrbit):
    pathArr = []
    if root.name == targetOrbit.name:
        pathArr.append(root)
    else:
        for subOrbit in root.orbiters:
            if len(getMatchingOrbits(targetOrbit, subOrbit)) > 0:
                pathArr.append(root)
                pathArr += path(subOrbit, targetOrbit)
    return pathArr


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

# orbitList[0].printOrbit()
# print(getIterativeDepth(orbitList[0], 0))

rootOrbit = orbitList[0]
# rootOrbit.printOrbit()
youOrbit = getMatchingOrbits(Orbit("YOU"), rootOrbit)[0]
santaOrbit = getMatchingOrbits(Orbit("SAN"), rootOrbit)[0]

youPath = path(rootOrbit, youOrbit)
santaPath = path(rootOrbit, santaOrbit)

commonIndex = 0
while youPath[commonIndex] == santaPath[commonIndex]:
    commonIndex += 1
#print(commonIndex, len(youPath), len(santaPath))

orbitalDistance = len(youPath) - commonIndex + len(santaPath) - commonIndex - 2
print(orbitalDistance)
