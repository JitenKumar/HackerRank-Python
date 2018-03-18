# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.
# Sample Input 0
#
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
#
# hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap_case(s):
    list = []
    for l in s:
        if l.islower():
            list.append(l.upper())
        elif l.isupper():
            list.append(l.lower())
        else:
            list.append(l)
    str1 = ''.join(str(e) for e in list)
    return str1