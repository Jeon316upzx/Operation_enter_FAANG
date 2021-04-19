'''
Given two strings, determine if the first string is an anagram of the second

'''


def valid_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    str1_dic = dict()

    for s1 in str1:
        if s1 in str1_dic.keys():
            str1_dic[s1] += 1
        else:
            str1_dic[s1] = 0

    print(str1_dic)

    for s2 in str2:
        if s2 in str1_dic.keys():
            if str1_dic[s2] < 0:
                return False
            else:
                str1_dic[s2] -= 1

    return True


print(valid_anagrams("iceman", "cinema"))
