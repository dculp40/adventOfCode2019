combos = 0
for i in range(246515, 739105):
    # for i in range(247990, 248000):
    # for i in range(111120, 123500):
    rawNum = i
    digits = []
    while rawNum > 9:
        lastDigit = rawNum % 10
        digits.insert(0, lastDigit)
        rawNum = (rawNum - lastDigit) / 10
    digits.insert(0, rawNum)

    increasing = True
    adjacency = False
    adjacencyCount = 1
    # print(i)
    for j in range(len(digits) - 1):
        left = digits[j]
        right = digits[j + 1]
        if right < left:
            increasing = False
            break
        if left == right:
            adjacencyCount += 1
            # if adjacencyCount > 2:
            #     adjacency = False
            #     break
        else:
            if adjacencyCount == 2:
                adjacency = True
            adjacencyCount = 1
        #print(digits[j+1], adjacency, adjacencyCount)
    if adjacencyCount == 2:
        adjacency = True

    if increasing & adjacency:
        combos += 1
        # print(i)


print(combos)
