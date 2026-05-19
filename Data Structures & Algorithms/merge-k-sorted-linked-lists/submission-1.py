# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergetwo(head1,head2):
            res=ListNode()
            dummy=res

            while head1 and head2:
                if head1.val<head2.val:
                    res.next=head1
                    head1=head1.next
                else:
                    res.next=head2
                    head2=head2.next
                res=res.next
            res.next = head1 or head2
            return dummy.next


        if not lists or len(lists)==0:
            return None
        
        
        while len(lists)>1:
            mergelists=[]
            for i in range(0,len(lists),2):    
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                mergelists.append(mergetwo(l1,l2))
            lists=mergelists
        return mergelists[0]


        
            
            
        