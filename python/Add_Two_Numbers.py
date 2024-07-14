# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def ll_iter(node):
        while node:
            yield node.val
            node = node.next
    ListNode.__iter__ = ll_iter

    def list_to_linked_list(self, nums: list) -> Optional[ListNode]:
        if not nums: 
            return None
        head = ListNode(nums[0])
        current = head
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list(l1)
        l2 = list(l2)

        l1.reverse()
        l2.reverse()
        result = []

        if len(l1) < len(l2):
            l1, l2 =  l2, l1
            
        flag = 0
        for index, value in enumerate(l1):
            if index+1 <= len(l2):
                if value == 0 or l2[index] == 0:
                    result = result + [0 + flag]
                    flag = 0
                elif (value + l2[index] + flag) / 10 < 1:
                    result = result + [value + l2[index] + flag]
                    flag = 0
                else:
                    result = result + [(value + l2[index] + flag) % 10 ]
                    flag = 1
            else:
                if (value + flag) / 10 < 1:
                    result = result + [value + flag]
                    flag = 0
                else:
                    result = result + [(value + flag) % 10]
            if index + 1 == len(l1) and result[-1] == 0 and flag == 1:
                result = result + [1]

        linked_list = self.list_to_linked_list(result)
    
        return linked_list
                
