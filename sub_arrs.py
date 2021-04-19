'''
Given an array, return all the sub arrays

'''


def sub_array(arr):
    if len(arr) <= 1:
        return arr
    sub_arr = []
    for i in range(len(arr) + 1):
        for j in range(i + 1, len(arr) + 1):
            chunks = arr[i:j]
            sub_arr.append(chunks)

    return sub_arr


print(sub_array([1, 2, 4, 5, 6, 7, 8]))
