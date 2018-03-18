# # You are given a string S.
# # Your task is to find out if the string S  contains:
# #  alphanumeric characters, alphabetical characters, digits,
# #  lowercase and uppercase characters.
# Input Format
#
# A single line containing a string .
#
# Constraints
#  0 < len(S) <1000
#
# Output Format
#
# In the first line, print True if S  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
#
# Sample Input
#
# qA2
# Sample Output
#
# True
# True
# True
# True
# True

# Functions

st = input()
l = [False, False, False, False, False,]
ls = [(s.isalnum(),s.isalpha(), s.isdigit(), s.islower(), s.isupper()) for s in st]
for lst in ls:
    for j in range(0,5):
        l[j] |= lst[j]

for i in range(0,5):
    print(l[i])