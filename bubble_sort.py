'''
Implementing Bubble sort

'''


def my_bubbler(nums):
    if len(nums) <= 1:
        return nums
    counter = 0
    for i in range(1, len(nums)):
        if nums[counter] > nums[i]:
            temp = nums[counter]
            nums[counter] = nums[i]
            nums[i] = temp

    return nums


print(my_bubbler([9, 3, 1, 0, 34]))
