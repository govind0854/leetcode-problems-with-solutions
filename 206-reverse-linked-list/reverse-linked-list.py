# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        lst=[]
        temp=head
        while temp!=None:
            lst.append(temp.val)
            temp=temp.next
        temp=head
        for i in range(len(lst)-1,-1,-1):
            temp.val=lst[i]
            temp=temp.next
        return head
        