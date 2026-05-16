# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        res=ListNode()

        while  fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None
        
        prev,curr=None,second

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            
        
        # l1,l2= head,prev

        while prev:
            temp1,temp2=head.next,prev.next
            head.next = prev 
            prev.next= temp1
            head,prev=temp1,temp2

        
        





        