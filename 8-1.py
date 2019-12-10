

with open('photoInput.txt', 'r') as open_file:
    encodedPhoto = []
    for line in open_file:
        encodedPhoto.append(line)

encodedPhoto = encodedPhoto[0]
#encodedPhoto = "123456789012"
print(encodedPhoto[0])

decodedPhoto = []

while len(encodedPhoto) > 0:
    layer = []
    for i in range(6):
        row = []
        for j in range(25):
            row.append(encodedPhoto[0])
            encodedPhoto = encodedPhoto[1:]

        layer.append(row)

    decodedPhoto.append(layer)

minZeros = float("inf")
for layer in decodedPhoto:
    digitCounts = [0] * 10
    for row in layer:
        for digit in row:
            digit = int(digit)
            digitCounts[digit] += 1
    if digitCounts[0] < minZeros:
        minZeros = digitCounts[0]
        print(digitCounts[1] * digitCounts[2])
