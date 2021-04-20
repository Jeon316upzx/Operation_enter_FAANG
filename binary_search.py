'''
Implement binary search

'''
import math


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    middle = math.floor((left + right) / 2)
    while nums[middle] != target and left <= right:
        if target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1
        middle = math.floor((left + right) / 2)

    if nums[middle] == target:
        return middle
    else:
        return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 50))
