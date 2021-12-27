# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#iteratively 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while (current != None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
#recursive+
class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if (head == None):
            return prev
        temp = head.next
        head.next = prev
        return self.reverseList(temp, head)
