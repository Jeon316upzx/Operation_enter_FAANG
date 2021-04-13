# def smallest_num(nums):
#     smallest = nums[0]
#     for i in nums:
#         if i < smallest:
#             smallest = i

#     print(smallest)


# smallest_num([2,34,5,6,3,2])


# o(n)
# def my_factorial(num):
#     if num == 1 or num == 0:
#         return 1
#     xfactorial = 1
#     for i in range(1, num):
#         xfactorial = xfactorial * i
#     return xfactorial


# print(my_factorial(9))


# def rfactorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * rfactorial(num - 1)


# print(rfactorial(64))
# print(rfactorial(8))

# print(rfactorial(64)/rfactorial(8))


# def revert(nums):
#     for i in range(1, len(nums)+1):
#         print(nums[-i])


# print(revert([1, 2, 3, 4, 5, 6])


# def duplicate_zeros(arr):
#     counter = 0
#     while counter < len(arr):
#         if arr[counter] == 0:
#             arr.pop()
#             arr.insert(counter + 1, 0)
#             counter += 2
#         else:
#             counter += 1
#     return arr


# print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))


def square_even_indexed_positions(nums):
    arr_len = len(nums)
    if arr_len < = 0:
        return "Array is empty"

    for i in range(arr_len):
        if i % 2 == 0:
            nums[i] *= nums[i]

    return nums
