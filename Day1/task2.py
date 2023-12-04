import re

print('\033[2J\033[H')
file = open('inputs.txt', 'r')
# file = open('Text.txt', 'r')
output = 0
conv = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def locate(line, digits):
    digits = re.findall(
        '(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    return digits


for line in file:
    if len(line) < 2:
        continue

    indexed = locate(line, conv)

    first = indexed[0]
    last = indexed[-1]

    if first in conv:
        first = conv[first]
    if last in conv:
        last = conv[last]

    print(int(first)*10 + int(last))

    output += int(first)*10 + int(last)

print(f'\nOUTPUT: {output}\n')
file.close()
