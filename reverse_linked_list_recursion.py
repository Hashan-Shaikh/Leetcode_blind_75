# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # Base case: If head is None or a single node
        if head is None or head.next is None:
            return head

        # Recursive case: Reverse the rest of the list
        reversed_head = self.reverseList(head.next)

        # Adjust the next pointer of the next node to point to the current node
        head.next.next = head
        head.next = None

        # Return the new head of the reversed list
        return reversed_head