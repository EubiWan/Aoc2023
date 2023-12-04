print('\033[2J\033[H')
file = open('inputs.txt', 'r')
output = 0
count = 0
colours = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def spliting_hairs(newline):
    data = []
    newlist = newline.split('; ')

    for ele in newlist:
        temp = ele.split(', ')

        for ment in temp:
            data.append(ment.split(' '))

    return data


def linecheck(data):
    count = 0
    for ele in data:
        if int(ele[0]) > colours[ele[1]]:
            count += 1
    if count > 0:
        return False

    else:
        return True


for line in file:
    count += 1

    temp = line.replace(f'Game {count}: ', '')
    newline = temp.replace('\n', '')

    data = spliting_hairs(newline)
    check = linecheck(data)
    if check:

        output += count


print(output)
