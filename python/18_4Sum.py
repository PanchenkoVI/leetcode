'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

import itertools

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        for item in itertools.combinations (nums, 4):
            if sum(item) == target:
                result += [list(item)]
        unique_list = set(tuple(lst) for lst in result)
        unique_list_for_list = [list(tpl) for tpl in unique_list]
        return unique_list_for_list
