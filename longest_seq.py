'''
Finding the longest sequence in an array
[1,24,5,6,4,3,5,89,34]
[3,4,5,6] == 4

'''

# Psuedocode
# This is a naive approach to this solution

#


def longest_seq(arr):
    # sort the array, that makes it easy to find consecutive items
    arr.sort()
    print(arr)
    # create two variables, One for longest streak and the other as a normal counter
    longest_streak = 0
    counter = 0

    for i in range(1, len(arr)):
        if arr[i] - arr[counter] == 1:
            longest_streak += 1
            counter += 1
        elif arr[i] - arr[counter] == 0:
            counter += 1
        else:
            counter += 1

    return longest_streak


print(longest_seq([1, 24, 5, 6, 4, 3, 5, 89, 34]))
