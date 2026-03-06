# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        place = 1
        #applying while loop1
        while l1:
            num1 += l1.val * place
            place *= 10
            l1 = l1.next
        
        place = 1
        #applying while loop2
        while l2:
            num2 += l2.val * place
            place *= 10
            l2 = l2.next
        
        total = num1 + num2
        
        if total == 0:
            return ListNode(0)
        
        head = None
        current = None
        
        while total > 0:
            digit = total % 10
            total //= 10
            
            node = ListNode(digit)
            
            if head is None:
                head = node
                current = node
            else:
                current.next = node
                current = current.next
        
        return head