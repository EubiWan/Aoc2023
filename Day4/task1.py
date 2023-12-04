import re

file = open('inputs.txt', 'r')
output = 0
count = 0

print('\033[2J\033[H')


def splitting_atoms(newline):
    data = []
    for item in newline:
        data.append(item.split(' '))

    for i in range(len(data)):
        for j in range(data[i].count('')):
            if count == 0:
                break
            else:
                data[i].remove('')

        for j in range(len(data[i])):
            if len(data[i][j]) == 1:
                data[i][j] = '0' + data[i][j]

    return data


for line in file:
    count += 1
    o = 0

    temp = line.replace(f'Card {count}: ', '')
    temp = temp.replace('\n', '')
    newline = temp.split(' | ')

    data = splitting_atoms(newline)

    for j in range(len(data[1])):
        if data[1][j] in data[0]:
            if o == 0:
                o += 1
            else:
                o *= 2

    output += o

print(output)
file.close()
