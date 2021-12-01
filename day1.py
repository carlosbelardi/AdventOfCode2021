def readFile(fileName):
    fileObj = open(fileName, 'r')
    words = fileObj.read().splitlines()
    fileObj.close()
    return words


def createArr(input):
    return map(int, readFile(input))


def createWindows(depth_arr):
    window_arr = []
    for i in range(0, len(depth_arr)-2):
        new_num = depth_arr[i]
        for j in range(i+1, i+3):
            new_num += depth_arr[j]
        window_arr.append(new_num)
    return window_arr


def solution(my_arr):
    larger_count = 0
    for i in range(1, len(my_arr)):
        if my_arr[i] > my_arr[i-1]:
            larger_count += 1
    return larger_count


print(solution(createArr('day1input.txt')))
print(solution(createWindows(createArr('day1input.txt'))))
