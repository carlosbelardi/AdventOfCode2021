def readFile(fileName):
    fileObj = open(fileName, 'r')
    directions = fileObj.read().splitlines()
    fileObj.close()
    return directions


binary_arr = readFile('day3input.txt')


def solution1(arr):
    frequency_dict = {}
    for i in range(0, len(arr[0])):
        frequency_dict[str(i)] = {'1': 0, '0': 0}
    for binary in arr:
        for bit in range(0, len(binary)):
            frequency_dict[str(bit)][binary[bit]] += 1

    gamma = ''
    epsilon = ''
    for j in range(0, len(arr[0])):
        my_max = max(frequency_dict[str(j)], key=frequency_dict[str(j)].get)
        my_min = min(frequency_dict[str(j)], key=frequency_dict[str(j)].get)
        gamma += str(my_max)
        epsilon += str(my_min)

    return int(gamma, 2) * int(epsilon, 2)


def solution2(arr):
    frequency_dict = {}
    for i in range(0, len(arr[0])):
        frequency_dict[str(i)] = {'1': 0, '0': 0}
    for binary in arr:
        for bit in range(0, len(binary)):
            frequency_dict[str(bit)][binary[bit]] += 1

    arr_copy_max = arr[:]
    arr_copy_min = arr[:]

    j = 0
    print(arr_copy_max)
    while len(arr_copy_max) > 1 and j < len(arr[0]):
        my_max = max(frequency_dict[str(j)], key=frequency_dict[str(j)].get)
        for item in arr_copy_max[:]:
            if item[j] != my_max:
                arr_copy_max.remove(item)
        j += 1

    k = 0
    while len(arr_copy_min) > 1 and k < len(arr[0]):
        my_min = min(frequency_dict[str(k)], key=frequency_dict[str(k)].get)
        for item in arr_copy_min[:]:
            if item[k] != my_min:
                arr_copy_min.remove(item)
        print('should keep these at index:', my_min, k)
        print(arr_copy_min)
        k += 1

    print(j, k, arr_copy_max, arr_copy_min)
    oxygen = arr_copy_max[0]
    co2 = arr_copy_min[0]

    return int(oxygen, 2) * int(co2, 2)


print('solution 1:', solution1(binary_arr))
print('solution 2:', solution2(binary_arr))
