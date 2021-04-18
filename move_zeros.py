'''
Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

'''


def move_zeros_back(nums):
    if len(nums) <= 1:
        return nums
    counter = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[counter] = nums[i]
            counter += 1

    while counter < len(nums):
        nums[counter] = 0
        counter += 1

    return nums


print(move_zeros_back([1, 0, 2, 3, 0, 0, 2, 3, 4, 5]))


"""

Given an integer array nums, move all 0's to the front of it while
maintaining the relative order of the non-zero elements.

"""


def move_zeros_front(nums):
    if len(nums) <= 1:
        return nums
    counter = len(nums) - 1
    for i in range(1, len(nums) + 1):
        if nums[-i] != 0:
            nums[counter] = nums[-i]
            counter -= 1

    while counter >= 0:
        nums[counter] = 0
        counter -= 1

    return nums


print(move_zeros_front([1, 0, 2, 3, 0, 0, 2, 3, 4, 5]))
