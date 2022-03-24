# Sort by Height

'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190]
'''


def solution(a):
    b = a.copy()
    t_dict = {}
    count = 0
    for x in b:
        if x == -1:
            t_dict.update({count: x})
        count += 1
        
    for x in t_dict:
        b.remove(-1)

    b.sort()
    print(b)
    for x in t_dict.keys():
        b.insert(x, -1)

    return b

