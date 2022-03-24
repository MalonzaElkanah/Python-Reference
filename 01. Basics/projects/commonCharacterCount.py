# commonCharacterCount

'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''


def solution(s1, s2):
    s1_arr = list(s1)
    s2_arr = list(s2)
    count = 0
    for x in s1_arr:
        try:
            s2_arr.remove(x)
            count += 1
        except Exception:
            pass
    
    return count



# TEST

