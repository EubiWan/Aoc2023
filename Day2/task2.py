import re

colours = ['red', 'green', 'blue']

file = open('inputs.txt', 'r')
count = 0
output = 0

print('\033[2J\033[H')


def spliting_hairs(newline):
    data = []
    newlist = newline.split('; ')

    for ele in newlist:
        temp = ele.split(', ')

        for ment in temp:
            data.append(ment.split(' '))

    return data


for line in file:
    count += 1
    temp = line.replace(f'Game {count}: ', '')
    line = temp.replace('\n', '')

    amount = []

    data = spliting_hairs(line)

    for colour in colours:
        highest = []
        for ele in data:
            if colour in ele[1]:
                if len(ele[0]) == 1:
                    ele[0] = '0'+ele[0]
                highest.append(ele[0])

        highest.sort(reverse=True)
        amount.append(f'{highest[0]}')

    output += int(amount[0])*int(amount[1])*int(amount[2])

print(output)
