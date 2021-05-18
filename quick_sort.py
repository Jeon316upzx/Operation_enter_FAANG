'''
Implementation of Quick sort

'''

import traceback

# Psuedocode
# Quick sort works on the login that given a sorted array and element A
# the elements on the left A are less than or equal element A and the ones of the right of A
# are greater than or equal A
# given arr = [1,2,3,4,5,6]
# where A = 4
# elements arr[:2] <= 4
# elements arr[4:] >= 4


def getPivot(arr):
    start = 0
    pivot = arr[start]
    indexGrtrPivot = 0
    for i in range(1, len(arr)):
        if pivot > arr[i]:
            print("{} > {}".format(pivot, arr[i]))
            indexGrtrPivot += 1
            print("Swap -> {} and {}".format(arr[i], arr[indexGrtrPivot]))
            temp = arr[indexGrtrPivot]
            print("temp {}".format(temp))
            arr[indexGrtrPivot] = arr[i]
            print("array at i{}".format(arr[i]))
            arr[i] = temp
    temp = arr[indexGrtrPivot]
    arr[indexGrtrPivot] = arr[start]
    arr[start] = temp
    print("after swap -> {}".format(arr))

    return indexGrtrPivot


# print(getPivot([5, 6]))


def quick_sort(arr):
    if len(arr) > 1:
        # print("Array before {}".format(arr))
        # print("left {} < right{}".format(left, right))
        pivot = getPivot(arr)
        print("PIVOOOOOOOOOOTTTTTT ->  {}  ".format(pivot))
        print("----------------------------------")
        print("slice left{}".format(arr[:pivot]))
        # print("slice right{}".format(arr[pivot+1:]))
        quick_sort(arr[:pivot])
    # quick_sort(arr[pivot+1:])
    # print("Array after{}".format(arr))
        return quick_sort(arr[:pivot])


# print(quick_sort([10, 5, 6, 9, 8, 30, 7, 27]))

print(quick_sort([4, 8, 2, 1, 5, 7, 6, 3]))
