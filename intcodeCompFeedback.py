

def splitSettings(settingsParam):
    settings = [settingsParam % 100]
    settingsParam = (settingsParam - settings[0]) / 100
    for _ in range(3):
        mode = settingsParam % 10
        settings.append(int(mode))
        settingsParam = (settingsParam - mode) / 10
    return settings


def runIntCode(intCode, instructionIndex=0):
    instructionIndex = instructionIndex
    inputCount = 0
    ampOutput = 0
    # [opcode, mode1, mode2, mode3]
    settings = splitSettings(intCode[instructionIndex])

    def getIndex(instructionOffset):
        mode = settings[instructionOffset]
        if mode == 0:  # position
            return intCode[instructionIndex + instructionOffset]
        else:  # immediate
            return instructionIndex + instructionOffset

    while settings[0] != 99:
        if settings[0] == 1:  # add values
            intCode[getIndex(3)] = intCode[getIndex(1)] + intCode[getIndex(2)]
            instructionIndex += 4
        elif settings[0] == 2:  # multiply valules
            intCode[getIndex(3)] = intCode[getIndex(1)] * intCode[getIndex(2)]
            instructionIndex += 4
        elif settings[0] == 3:  # save input
            if (inputCount == 0):
                intCode[getIndex(1)] = phaseSettings[ampCount]
                inputCount += 1
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

        settings = splitSettings(intCode[instructionIndex])
    if ampCount == 4:
        return ampOutput
    return runIntCode(MASTER_INTCODE.copy(), ampCount + 1, phaseSettings, ampOutput)


def getPhaseSettings():
    allPhaseSettings = []
    for a in range(5, 10):
        for b in range(5, 10):
            for c in range(5, 10):
                for d in range(5, 10):
                    for e in range(5, 10):
                        phaseSettings = [a, b, c, d, e]
                        if (len(phaseSettings) == len(set(phaseSettings))):
                            allPhaseSettings.append(phaseSettings)
    return allPhaseSettings


def getOutput(phaseSettings):
    while len(IOs) > 0:
        tryPhaseSettings(phaseSettings)
        newOutput = runIntCode(
            MASTER_INTCODE.copy(), 0, phaseSettings, 0)
        # print(IOs)
        if newOutput > maxOutput:
            maxOutput = newOutput
            maxPhaseSettings = phaseSettings
    print(maxPhaseSettings, maxOutput)


INTCODE_STRING = "3,8,1001,8,10,8,105,1,0,0,21,38,63,88,97,118,199,280,361,442,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,101,3,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,3,9,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99"
DIAGS = [["3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5",
          [9, 8, 7, 6, 5], 139629729],
         ["3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10",
          [9, 7, 8, 5, 6], 18216]]

MASTER_INTCODES = []
IOs = [0, 0]
CurrentAmp = 0


for test in DIAGS:
    MASTER_INTCODES = [int(i) for i in test[0].split(',')] * 5
    findMaxOutput()
    print(runIntCode(MASTER_INTCODE.copy(), 0, test[1], 0), test[2])
    #print(runIntCode(MASTER_INTCODE.copy(), 0, [4, 4, 4, 4, 4], 0), test[2])

MASTER_INTCODE = [int(i) for i in INTCODE_STRING.split(',')]
findMaxOutput()

# phaseSettings = [0] * 5
# print(maxOutput)
# print(trialCount)
