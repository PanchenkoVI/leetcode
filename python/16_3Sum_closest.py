'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

import itertools
import numpy as np

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        new_lst = list(itertools.combinations(nums,3))
        result = [np.inf]
        for lst in new_lst:
            if abs(sum(lst) - target) <= sum(result) and abs(sum(lst) - target) <= target:
                result = list(lst)
                result_sum = sum(lst)
        return result_sum
