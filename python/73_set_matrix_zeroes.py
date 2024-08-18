'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        result = []
        ind_str = []
        ind_column = []
        
        for ind, lst in enumerate(matrix):
            for ind2,l in enumerate(lst):
                if l == 0:
                    ind_column += [ind2]
                    ind_str += [ind]
            result += [lst]
        matrix = result
        result = []
            
        for ind, lst in enumerate(matrix):
            if ind in ind_str:
                result += [[ 0 for i in lst]]
                continue
            for ind2, lst2 in enumerate(lst):
                if ind2 in ind_column:
                    lst[ind2] = 0
            result += [[ i for i in lst]]
        print(result)
        
