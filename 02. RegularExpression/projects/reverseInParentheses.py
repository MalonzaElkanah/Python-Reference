# reverseInParentheses

'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

    For inputString = "(bar)", the output should be
    solution(inputString) = "rab";

    For inputString = "foo(bar)baz", the output should be
    solution(inputString) = "foorabbaz";

    For inputString = "foo(bar)baz(blim)", the output should be
    solution(inputString) = "foorabbazmilb";

    For inputString = "foo(bar(baz))blim", the output should be
    solution(inputString) = "foobazrabblim".
    Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim"
'''

import re

def solution(text):
    loops = text.count('(')
    for x in range(0, loops):
        pattern = re.compile(r'\([a-zA-Z]+\)')
        strings = re.findall(pattern, text)
        for string in strings:
            arr = list(string)
            arr2 = arr.copy()
            arr.reverse()
            string2 = ''
            for x in arr:
                if x not in ['(', ')']:
                    string2 += x
            string3 = ''
            for x in arr2:
                if x not in ['(', ')']:
                    string3 += x

            pattern2 = re.compile(r'\('+string3+r'\)')
            print('{}, {}'.format(string, string2))
            text = pattern2.sub(string2, text)
    return text

print("-------")
ARR = ["foo(bar)baz(blim)", "foo(bar(baz))blim"]
for x in ARR:
    y = solution(x)
    print('{}: {}'.format(x, y))
