# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        lst=[]
        temp=head
        while temp!=None:
            lst.append(temp.val)
            temp=temp.next
        temp=head
        left=0
        right=len(lst)-1
        while left < right:
            if lst[left]!=lst[right]:
                return False
            left +=1
            right -=1
        return True
            
       