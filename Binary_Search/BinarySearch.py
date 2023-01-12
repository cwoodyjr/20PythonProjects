def binarySearch(list, element):
    start = 0
    middle = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print('Step', steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle-1
        else:
            start = middle+1
    return -1


numList = [1, 2, 3, 4, 5]
target = 4
binarySearch(numList, target)
