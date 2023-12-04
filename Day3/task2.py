import re

print('\033[2J\033[H')

data = []
output = 0


def numfinder(a, b, data):
    # global data
    fullnumber = str(data[a][b])

    if data[a][b-1].isdigit() and b-1 != 0:
        fullnumber = str(data[a][b-1]) + fullnumber
        data[a][b-1] = '.'

        if data[a][b-2].isdigit() and b-2 != len(data[a]):
            fullnumber = str(data[a][b-2]) + fullnumber
            data[a][b-2] = '.'

    if data[a][b+1].isdigit() and b+1 != len(data[a]):
        fullnumber = fullnumber + str(data[a][b+1])
        data[a][b+1] = '.'

        if data[a][b+2].isdigit() and b+2 != len(data[a]):
            fullnumber = fullnumber + str(data[a][b+2])
            data[a][b+2] = '.'

    # print(fullnumber)
    return fullnumber


with open('inputs.txt', 'r') as f:
    temp = f.read().split('\n')

for line in temp:
    data.append(list(line))

for i in range(len(data)):
    for j in range(len(data[i])):
        count = 0
        if data[i][j] == '*':
            place = []
            if data[i+1][j].isdigit():
                count += 1
                place.append(numfinder(i+1, j, data))

            if data[i+1][j+1].isdigit() and j < len(data[i]):
                count += 1
                place.append(numfinder(i+1, j+1, data))

            if data[i][j+1].isdigit() and j < len(data[i]):
                count += 1
                place.append(numfinder(i, j+1, data))

            if data[i-1][j+1].isdigit() and j < len(data[i]):
                count += 1
                place.append(numfinder(i-1, j+1, data))

            if data[i-1][j].isdigit():
                count += 1
                place.append(numfinder(i-1, j, data))

            if data[i-1][j-1].isdigit() and j > 0:
                count += 1
                place.append(numfinder(i-1, j-1, data))

            if data[i][j-1].isdigit() and j > 0:
                count += 1
                place.append(numfinder(i, j-1, data))

            if data[i+1][j-1].isdigit() and j > 0:
                count += 1
                place.append(numfinder(i+1, j-1, data))

            # print(count, place)

        if count == 2:
            temp = int(place[0]) * int(place[1])
            # print(temp)
            output += temp

print(output)
