

with open('photoInput.txt', 'r') as open_file:
    encodedPhoto = []
    for line in open_file:
        encodedPhoto.append(line)

#ncodedPhoto = "0222112222120000"
encodedPhoto = encodedPhoto[0]

layeredPhoto = []
height = 6
width = 25

while len(encodedPhoto) > 0:
    layer = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(encodedPhoto[0])
            encodedPhoto = encodedPhoto[1:]

        layer.append(row)

    layeredPhoto.append(layer)

minZeros = float("inf")
for layer in layeredPhoto:
    digitCounts = [0] * 10
    for row in layer:
        for digit in row:
            digit = int(digit)
            digitCounts[digit] += 1
    if digitCounts[0] < minZeros:
        minZeros = digitCounts[0]
        print(digitCounts[1] * digitCounts[2])

print(layeredPhoto)
finalImage = [[' ' for i in range(width)] for j in range(height)]

for k in range(len(layeredPhoto)):
    layer = layeredPhoto[len(layeredPhoto) - k - 1]
    for j in range(len(layer)):
        for i in range(len(layer[j])):
            pixel = layer[j][i]
            if int(pixel) < 2:
                finalImage[j][i] = pixel

for row in finalImage:
    s = ""
    for pixel in row:
        if pixel == '0':
            s += ' '
        else:
            s += '*'
    print(s)
