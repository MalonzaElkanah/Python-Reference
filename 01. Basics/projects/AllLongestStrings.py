# All Longest Strings

'''
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
'''

def solution(inputArray):
    data = {}
    count = []
    for arr in inputArray:
        size = len(arr)
        size_arr = data.get(size, [])
        size_arr.append(arr)
        
        data.update({size: size_arr})
        if size not in count:
            count.append(size)
        
    return data.get(max(count), [])



# TEST

