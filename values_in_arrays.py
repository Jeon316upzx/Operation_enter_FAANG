'''
Given two arrays, return True if all the values in arr1 has a squared value in the
second array arr2, if frequency is not important

'''


def arr1_squared_in_arr2(arr1, arr2):
    # naive solution
    if len(arr1) != len(arr2):
        return False
    for ar1 in arr1:
        if ar1 * ar1 not in arr2:
            return False
    return True


print(arr1_squared_in_arr2([1, 2, 3, 4, 5], [1, 4, 9, 16, 45]))
