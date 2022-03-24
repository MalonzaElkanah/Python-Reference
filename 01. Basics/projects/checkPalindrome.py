# checkPalindrome


'''
Given the string, check if it is a palindrome.

Example

    For inputString = "aabaa", the output should be
    solution(inputString) = true;
    For inputString = "abac", the output should be
    solution(inputString) = false;
    For inputString = "a", the output should be
    solution(inputString) = true.
'''

def solution(inputString):
    num = len(inputString)
    pal = num//2
    if num > 1:
        for x in range(0, pal+1):
            first = inputString[x]
            last = inputString[-(x+1)]
            if first != last:
                return False
        return True
    else:
        first = inputString[0]
        last = inputString[-1]
        if first == last:
            return True
        
    return False


# TEST
inputStrings = ["aabaa", "abac", "a"]
for inputString in inputStrings:
    bol = solution(inputString)
    print("INPUT: {}, PALINDROME?: {}".format(inputString, bol))