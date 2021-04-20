'''
Implementing Bubble sort

'''


def my_bubbler(nums):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            print(nums[j], nums[j+1], "old values")
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j+1] = temp
            print(nums[j], nums[j+1], "new values")

    return nums


print(my_bubbler([3, 4, 56, 23, 12, 9, 3, 1, 0, 34]))
