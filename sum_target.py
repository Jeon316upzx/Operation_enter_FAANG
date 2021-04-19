'''
Given an unsorted array, return the sub arrays that sum upto a target e.g
[1,3,4,5,6,3,7,2] 
target = 8

[3, 5]
[7, 1]
[6, 2]
[1, 3, 4]
'''


def sum_target(arr, target):
    if len(arr) <= 1:
        return "Array length has to be greater than two"
    sub_arrs = []
    for s in range(len(arr) + 1):
        for u in range(s + 1, len(arr) + 1):
            chunk = arr[s:u]
            sum = 0
            for c in chunk:
                sum += c
            # add restrictions as to what length gets returned eg
            # and len(chunk) == 1,2,3,4 etc
            if sum == target:
                sub_arrs.append(chunk)
                print(chunk, sum)

    return sub_arrs


print(sum_target([1, 2, 3, 4, 5, 6, 7], 9))
