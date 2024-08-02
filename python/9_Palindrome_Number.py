class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        lst = []
        lst.extend(str(x))
        lst.reverse()
        lst = ''.join(lst)
        if int(lst) == x:
            return True
        return False
        
