'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
'''

class Solution:
    def addDigits(self, num: int) -> int:
        result = []
        for i in str(num):
            result = result + [i]
        result = [ int(i) for i in result ]
        if len(str(sum(result))) > 1:
            result2 = []
            for i in str(sum(result)):
                result2 = result2 + [i]
            result2 = [ int(i) for i in result2 ]
            return sum(result2)
        else:
            return sum(result)
