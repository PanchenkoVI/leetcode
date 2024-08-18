'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

    result = []
    iter_max = 0
    iter_min = 0
    flag = 0
    for ind, row in enumerate(intervals): 
        if iter_max >= min(row):
            result[flag-1] = [iter_min, max(row)]
            iter_max = max(row)
            iter_min = min(row)
            continue
        flag += 1
        iter_min = min(row)
        iter_max = max(row)
        result += [row]    
    return result
