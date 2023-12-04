file = open('inputs.txt', 'r')
output = 0

for line in file:
    temp = ''

    for letter in line:
        if letter.isnumeric():
            temp += str(letter)

    output += int(str(temp[0])+str(temp[-1]))

print(f'\nOUTPUT: {output}\n')
file.close()
