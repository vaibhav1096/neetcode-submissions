# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry=0

        # print(l_1.next.val,l_2.next.val)

        res=ListNode()
        dummy=res
        while l1 or l2 or carry:
            l1_val=l1.val if l1 else 0
            l2_val=l2.val if l2 else 0

            sum_ = l1_val + l2_val +carry
            carry=sum_//10
            value=sum_%10

            res.next=ListNode(value)
            res=res.next

            l1,l2=l1.next if l1 else None,l2.next if l2 else None
        
    
        return dummy.next
        
        



        