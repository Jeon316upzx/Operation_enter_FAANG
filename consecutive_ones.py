'''
Finding the longest sequence in 1s an array
[1,1,0,1,1,1,1,0] == 4

'''


# has unhandled edge case
def consecutive_ones(nums):
    if len(nums) <= 1:
        return nums

    counter = 0
    longest_ones = 0

    for i in range(1, len(nums)):
        if nums[counter] - nums[i] == 0:
            print("{} - {}".format(nums[counter], nums[i]))
            longest_ones += 1
            counter += 1
        else:
            counter += 1

    return longest_ones + 1


print(consecutive_ones([1, 0, 1, 1, 1, 1, 1, 1, 0]))


def actual_consecutive_ones(nums):
    counter = 0
    longest_streak = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            counter += 1
            longest_streak = max(longest_streak, counter)
        else:
            counter = 0

    return longest_streak


print(actual_consecutive_ones([1, 0, 1, 1, 1, 1, 1, 1, 0]))
