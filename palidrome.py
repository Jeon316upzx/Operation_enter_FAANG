'''
Given two strings, determine if the two strings are palindromes

'''


def valid_palindromes(str1, str2):
    if len(str1) != len(str2):
        return False

    if len(str1) <= 1 and len(str2) <= 1:
        return True

    if str1 == str2[::-1]:
        return True
    else:
        return False


print(valid_palindromes("cinema", "iceman"))
