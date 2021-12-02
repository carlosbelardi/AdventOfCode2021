def readFile(fileName):
    fileObj = open(fileName, 'r')
    directions = fileObj.read().splitlines()
    fileObj.close()
    return directions


instructions_arr = readFile('day2input.txt')


def solution1(instructions):
    dir_dict = {'forward': 0, 'up': 0, 'down': 0}
    for step in instructions:
        direction = step.split()[0]
        amount = int(step.split()[1])
        dir_dict[direction] += amount
    forward = dir_dict['forward']
    horizontal = dir_dict['down'] - dir_dict['up']
    return forward * horizontal


def solution2(instructions):
    horizontal = 0
    depth = 0
    aim = 0
    for step in instructions:
        direction = step.split()[0]
        amount = int(step.split()[1])
        if direction == 'down':
            aim += amount
        if direction == 'up':
            aim -= amount
        if direction == 'forward':
            horizontal += amount
            depth += aim * amount

    return horizontal * depth


print(solution1(instructions_arr))
print(solution2(instructions_arr))
