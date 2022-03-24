# adjacentElementsProduct

'''
Given an array of integers, 
find the pair of adjacent elements that has the largest product and return that product.

Example:

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
'''

def solution(inputArray):
    buffer = []
    num = len(inputArray)
    for x in range(0, num):
        if (x+1) < num:  
           buffer += [inputArray[x] * inputArray[x+1]]
    
    return max(buffer)


# TEST
ARR = [[3, 6, -2, -5, 7, 3], [-1, -2], [5, 1, 2, 3, 1, 4], 
	[1, 2, 3, 0], [5, 6, -4, 2, 3, 2, -23], 
	[4, 1, 2, 3, 1, 5], [-23, 4, -3, 8, -12], [1, 0, 1, 0, 1000]
]

for inputArray in ARR:
	k = solution(inputArray)
	print("ARRAY: {}, PRODUCT: {}".format(inputArray, k))

	