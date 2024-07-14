class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if value + value2 == target and index2 != index:
                    return(index, index2)

