'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
 
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
'''

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
        
        dummy = ListNode()
        current = dummy
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        return dummy.next
