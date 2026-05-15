# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        Nodeset=set()
        n=head
        while n:
            if n in Nodeset:
                return True
            Nodeset.add(n)
            n=n.next
        return False

