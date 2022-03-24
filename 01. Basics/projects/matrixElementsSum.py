# matrixElementsSum
'''
After becoming famous, the CodeBots decided to move into a new building together. 
Each of the rooms has a different cost, and some of them are free, 
but there's a rumour that all the free rooms are haunted! 
Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, 
or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, 
your task is to return the total sum of all rooms that are suitable for the CodeBots 
(ie: add up all the values that don't appear below a 0).

Example
For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

the output should be
solution(matrix) = 9
Thus, the answer is 1 + 5 + 1 + 2 = 9.

For

matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]

the output should be
solution(matrix) = 9
Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.
'''

def solution(matrix):
    blacklist = []
    arr = []
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            if matrix[x][y] == 0:
                blacklist.append(y)
            elif y not in blacklist:
                arr.append(matrix[x][y])
    
    return sum(arr)
MATRICE = [
	[[0,1,1,2], 
	 [0,5,0,0], 
	 [2,0,3,3]],

	[[1, 1, 1, 0], 
	 [0, 5, 0, 1], 
	 [2, 1, 3, 10]],

	[[1]],

	[[4,0,1], 
	 [10,7,0], 
	 [0,0,0], 
	 [9,1,2]],

	[[2], 
	 [5], 
	 [10]],

	 [[1,2,3,4,5]],
]

for matrix in MATRICE:
	results = solution(matrix)
	print("MATRIX {}, SUM: {}".format(matrix, results))



