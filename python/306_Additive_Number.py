'''
n additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199

'''

class Solution:
    def is_valid(self, num1, num2, remaining):
        while remaining:
            next_num = str(int(num1) + int(num2))
            if not remaining.startswith(next_num):
                return False
            remaining = remaining[len(next_num):]
            num1, num2 = num2, next_num
        return True    
    
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2 = num[:i], num[i:j]
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                if self.is_valid(num1, num2, num[j:]):
                    return True
        return False

