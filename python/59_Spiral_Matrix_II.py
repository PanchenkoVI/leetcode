'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Input: n = 1
Output: [[1]]

n = 3
Output: [[1,2],[4,3]]

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Input: n = 4
Output: [[ 1, 2, 3, 4],[12,13,14, 5], [11,16,15, 6], [10, 9, 8, 7]]
'''

def generateMatrix(n: int) -> list:
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    return matrix
