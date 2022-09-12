'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        counter = 0
        while True:
            counter += 1
            #pointer changes value every two steps (thanks to counter)
            #thus, at the end of the nth iteration, pointer will point at (n/2)th + 1 position
            if counter %2 == 0:
                pointer = pointer.next
            if head.next == None:
                break
            head = head.next
            
        return pointer
      
'''
Time complexity: O(n)
Space complexity: O(1)
'''
