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

    return int(fullnumber)


with open('inputs.txt', 'r') as f:
    temp = f.read().split('\n')

for line in temp:
    data.append(list(line))

for i in range(len(data)):
    for j in range(len(data[i])):
        if (not data[i][j].isalnum()) and data[i][j] != '.':
            if data[i+1][j].isdigit():
                number = numfinder(i+1, j, data)
                data[i+1][j] = '.'
                output += number

            if data[i+1][j+1].isdigit() and j != len(data[i]):
                number = numfinder(i+1, j+1, data)
                data[i+1][j+1] = '.'
                output += number

            if data[i][j+1].isdigit() and j != len(data[i]):
                number = numfinder(i, j+1, data)
                data[i][j+1] = '.'
                output += number

            if data[i-1][j+1].isdigit() and j != len(data[i]):
                number = numfinder(i-1, j+1, data)
                data[i-1][j+1] = '.'
                output += number

            if data[i-1][j].isdigit():
                number = numfinder(i-1, j, data)
                data[i-1][j] = '.'
                output += number

            if data[i-1][j-1].isdigit() and j != 0:
                number = numfinder(i-1, j-1, data)
                data[i-1][j-1] = '.'
                output += number

            if data[i][j-1].isdigit() and j != 0:
                number = numfinder(i, j-1, data)
                data[i][j-1] = '.'
                output += number

            if data[i+1][j-1].isdigit() and j != 0:
                number = numfinder(i+1, j-1, data)
                data[i+1][j-1] = '.'
                output += number

print(output)
