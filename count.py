'''
Given a character return the count of each character in the string

'''


def count_characters(str):
    count_obj = dict()
    for s in str:
        if s in count_obj.keys():
            count_obj[s] += 1
        else:
            count_obj[s] = 0

    return count_obj


print(count_characters("masterfully"))
