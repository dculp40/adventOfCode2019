
INTCODE_STRING = "3,8,1001,8,10,8,105,1,0,0,21,38,63,88,97,118,199,280,361,442,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,101,3,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,3,9,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99"
DIAGS = [["3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0",
          [4, 3, 2, 1, 0], 43210],
         ["3,23,3,24,1002,24,10,24,1002,23,-1,23, 101,5,23,23,1,24,23,23,4,23,99,0,0",
          [0, 1, 2, 3, 4], 54321],
         ["3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0", [1, 0, 4, 3, 2], 65210]]
MASTER_INTCODE = []


def splitSettings(settingsParam):
    settings = [settingsParam % 100]
    settingsParam = (settingsParam - settings[0]) / 100
    for _ in range(3):
        mode = settingsParam % 10
        settings.append(int(mode))
        settingsParam = (settingsParam - mode) / 10
    return settings


def runIntCode(intCode, ampCount, phaseSettings, ampInput):
    instructionIndex = 0
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
        elif settings[0] == 3:  # save input to instructionIndexition
            # usrInput = int(input("Input: "))
            # intCode[getIndex(1)] = usrInput
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


def findMaxOutput():
    maxOutput = 0
    maxPhaseSettings = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        phaseSettings = [a, b, c, d, e]
                        if (len(phaseSettings) == len(set(phaseSettings))):
                            newOutput = runIntCode(
                                MASTER_INTCODE.copy(), 0, phaseSettings, 0)
                            # print(IOs)
                            if newOutput > maxOutput:
                                maxOutput = newOutput
                                maxPhaseSettings = phaseSettings
    print(maxPhaseSettings, maxOutput)


for test in DIAGS:
    MASTER_INTCODE = [int(i) for i in test[0].split(',')]
    findMaxOutput()
    print(runIntCode(MASTER_INTCODE.copy(), 0, test[1], 0), test[2])
    #print(runIntCode(MASTER_INTCODE.copy(), 0, [4, 4, 4, 4, 4], 0), test[2])

MASTER_INTCODE = [int(i) for i in INTCODE_STRING.split(',')]
findMaxOutput()

# phaseSettings = [0] * 5
# print(maxOutput)
# print(trialCount)
