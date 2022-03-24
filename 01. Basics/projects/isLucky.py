# isLucky

'''
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    solution(n) = true;
    For n = 239017, the output should be
    solution(n) = false.

'''

def solution(n):
    char_n = str(n)
    arr_n = list(char_n)
    len_arr = len(arr_n)
    half_len = len_arr//2
    sum1 = 0
    sum2 = 0
    for x in range(0, half_len):
        sum1 += int(arr_n[x])
    
    for x in range(half_len, len_arr):
        sum2 += int(arr_n[x])
    
    return sum1 == sum2


# TEST

