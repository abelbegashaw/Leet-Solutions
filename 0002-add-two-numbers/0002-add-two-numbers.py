# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        list1, list2 = l1, l2
        curr = result
        carry = 0
        while list1 or list2 or carry:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0
            newNode = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) // 10
            if list1: list1 = list1.next
            if list2: list2 = list2.next
            curr.next = newNode
            curr = curr.next
        return result.next
