'''
Given an array, count the unique values

'''


def unique_value(arr):
    if len(arr) <= 1:
        return arr

    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return arr[:i+1]


print(unique_value([1, 1, 2, 2, 4, 5, 6, 6, 7]))
