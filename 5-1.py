INPUT_STRING = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,17,65,225,102,21,95,224,1001,224,-1869,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,101,43,14,224,1001,224,-108,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,57,94,225,1101,57,67,225,1,217,66,224,101,-141,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1102,64,34,225,1101,89,59,225,1102,58,94,225,1002,125,27,224,101,-2106,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1102,78,65,225,1001,91,63,224,101,-127,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1102,7,19,224,1001,224,-133,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,2,61,100,224,101,-5358,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,19,55,224,101,-74,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1101,74,68,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,677,224,102,2,223,223,1006,224,329,1001,223,1,223,1008,226,677,224,102,2,223,223,1006,224,344,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,374,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,434,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,479,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,524,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,569,101,1,223,223,1007,677,677,224,102,2,223,223,1005,224,584,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,599,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,108,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,644,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,659,101,1,223,223,1107,226,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226"
# "1,1,1,4,99,5,6,0,99"  # 30,1,1,4,2,5,6,0,99
# "1002,4,3,4,33"  # 1002,4,3,4,99
# "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9" # output 1 for nonzero
# "3,3,1105,-1,9,1101,0,0,12,4,12,99,1 # output 1 for nonzero
# "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99" #100 +/- 1 depending on over/under 8

stringArr = INPUT_STRING.split(',')
sequence = [int(i) for i in stringArr]


def getIndex(instructionOffset):
    mode = settings[instructionOffset]
    if mode == 0:  # position
        return sequence[instructionIndex + instructionOffset]
    else:  # immediate
        return instructionIndex + instructionOffset


def splitSettings(settingsParam):
    settings = [settingsParam % 100]
    settingsParam = (settingsParam - settings[0]) / 100
    for _ in range(3):
        mode = settingsParam % 10
        settings.append(int(mode))
        settingsParam = (settingsParam - mode) / 10
    return settings


instructionIndex = 0
# [opcode, mode1, mode2, mode3]
settings = splitSettings(sequence[instructionIndex])

while settings[0] != 99:

    if settings[0] == 1:  # add values
        sequence[getIndex(3)] = sequence[getIndex(1)] + sequence[getIndex(2)]
        instructionIndex += 4
    elif settings[0] == 2:  # multiply valules
        sequence[getIndex(3)] = sequence[getIndex(1)] * sequence[getIndex(2)]
        instructionIndex += 4
    elif settings[0] == 3:  # save input to instructionIndexition
        usrInput = int(input("Input: "))
        sequence[getIndex(1)] = usrInput
        instructionIndex += 2
    elif settings[0] == 4:  # output value
        print("Output: " + str(sequence[getIndex(1)]))
        instructionIndex += 2
    elif settings[0] == 5:  # jump-if-true
        if sequence[getIndex(1)] != 0:
            instructionIndex = sequence[getIndex(2)]
        else:
            instructionIndex += 3
    elif settings[0] == 6:  # jump-if-false
        if sequence[getIndex(1)] == 0:
            instructionIndex = sequence[getIndex(2)]
        else:
            instructionIndex += 3
    elif settings[0] == 7:  # less than
        if sequence[getIndex(1)] < sequence[getIndex(2)]:
            sequence[getIndex(3)] = 1
        else:
            sequence[getIndex(3)] = 0
        instructionIndex += 4
    else:  # equals
        if sequence[getIndex(1)] == sequence[getIndex(2)]:
            sequence[getIndex(3)] = 1
        else:
            sequence[getIndex(3)] = 0
        instructionIndex += 4

    settings = splitSettings(sequence[instructionIndex])

# while settings[0] != 99:
#     if settings[0] == 1:
#         sequence[sequence[instructionIndex+3]] = sequence[sequence[instructionIndex + 1]] + \
#             sequence[sequence[instructionIndex + 2]]
#     else:
#         sequence[sequence[instructionIndex+3]] = sequence[sequence[instructionIndex + 1]] * \
#             sequence[sequence[instructionIndex + 2]]
#     instructionIndex += 4
#     settings[0] = sequence[instructionIndex]
# return sequence[0]
