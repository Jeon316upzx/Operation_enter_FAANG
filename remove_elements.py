'''
Given an array nums and a value val, 
remove all instances of that value in-place and return the new length.

'''


def remove_element(arr, val):
    counter = 0
    for i in range(len(arr)):
        if val != arr[i]:
            arr[counter] = arr[i]
            counter += 1

    return arr


print(remove_element([2, 3, 3, 3, 6],  3))
print(remove_element([2, 3, 4, 5, 5, 6, 0, 5, 5],  5))
