
def splitOpcodeParam(opcodeParam):
    settings = [opcodeParam % 100]
    opcodeParam = (opcodeParam - settings[0]) / 100
    for _ in range(3):  # [opcode, mode1, mode2, mode3]
        settings.append(int(opcodeParam % 10))  # mode: position/immediate
        opcodeParam = (opcodeParam - (opcodeParam % 10)) / 10
    return settings


# intCodeContext: [intCode, instructionIndex, phase, phaseIsSet, ampInput, ampID]
def runIntCode(intCodeContext):
    global contextManager

    intCode, instructionIndex, phase, phaseIsSet, ampInput, ampID = intCodeContext
    #nextContext = intCodeContexts[(ampID+1 % 5)]
    ampOutput = None

    settings = splitOpcodeParam(intCode[instructionIndex])

    def getIndex(instructionOffset):
        mode = settings[instructionOffset]
        if mode == 0:  # position
            return intCode[instructionIndex + instructionOffset]
        else:  # immediate
            return instructionIndex + instructionOffset

    while settings[0] != 99 and not ampOutput:
        if settings[0] == 1:  # add values
            intCode[getIndex(3)] = intCode[getIndex(1)] + intCode[getIndex(2)]
            instructionIndex += 4
        elif settings[0] == 2:  # multiply valules
            intCode[getIndex(3)] = intCode[getIndex(1)] * intCode[getIndex(2)]
            instructionIndex += 4
        elif settings[0] == 3:  # save input
            if not phaseIsSet:
                intCode[getIndex(1)] = phase
                phaseIsSet = True
            else:
                intCode[getIndex(1)] = ampInput
            instructionIndex += 2
        elif settings[0] == 4:  # output value
            # print("Output: " + str(intCode[getIndex(1)]))
            ampOutput = intCode[getIndex(1)]
            instructionIndex += 2
        elif settings[0] == 5:  # jump-if-true
            if intCode[getIndex(1)] != 0:
                instructionIndex = intCode[getIndex(2)]
            else:
                instructionIndex += 3
        elif settings[0] == 6:  # jump-if-false
            if intCode[getIndex(1)] == 0:
                instructionIndex = intCode[getIndex(2)]
            else:
                instructionIndex += 3
        elif settings[0] == 7:  # less than
            if intCode[getIndex(1)] < intCode[getIndex(2)]:
                intCode[getIndex(3)] = 1
            else:
                intCode[getIndex(3)] = 0
            instructionIndex += 4
        else:  # equals
            if intCode[getIndex(1)] == intCode[getIndex(2)]:
                intCode[getIndex(3)] = 1
            else:
                intCode[getIndex(3)] = 0
            instructionIndex += 4

        settings = splitOpcodeParam(intCode[instructionIndex])

    contextManager[ampID] = [intCode, instructionIndex,
                             phase, phaseIsSet, ampInput, ampID]

    if ampOutput:
        nextAmp = (ampID + 1) % 5
        contextManager[nextAmp][4] = ampOutput
        return runIntCode(contextManager[nextAmp])
    return ampInput


def getPhaseCombos(start, end):
    phaseCombos = []
    for a in range(start, end):
        for b in range(start, end):
            for c in range(start, end):
                for d in range(start, end):
                    for e in range(start, end):
                        phaseIsSettings = [a, b, c, d, e]
                        if (len(phaseIsSettings) == len(set(phaseIsSettings))):
                            phaseCombos.append(phaseIsSettings)
    return phaseCombos


def contextSetup(phases):
    newContexts = []
    for i in range(5):
        context = [MASTER_INTCODE.copy(), 0, phases[i], False, 0, i]
        newContexts.append(context)
    return newContexts


def getBestPhases(phasesToTry):
    global contextManager
    maxPower = 0
    bestPhases = []
    for phaseSettings in phasesToTry:
        contextManager = contextSetup(phaseSettings)
        newPower = runIntCode(contextManager[0])
        if newPower > maxPower:
            maxPower = newPower
            bestPhases = phaseSettings
    return (bestPhases, maxPower)


INTCODE_STRING = "3,8,1001,8,10,8,105,1,0,0,21,38,63,88,97,118,199,280,361,442,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,101,3,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,3,9,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99"

MASTER_INTCODE = [int(i) for i in INTCODE_STRING.split(',')]

# intCodeContext: [intCode, instructionIndex, phase, phaseIsSet, ampInput, ampID]
contextManager = []

phaseCombos = getPhaseCombos(5, 10)
print(getBestPhases(phaseCombos))
