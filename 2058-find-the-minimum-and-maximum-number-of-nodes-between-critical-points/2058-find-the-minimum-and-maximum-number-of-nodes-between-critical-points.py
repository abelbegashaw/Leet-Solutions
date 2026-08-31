# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        prev, curr = head, head.next
        result = [float('inf'), -1]
        index = 1
        first_index = -1
        last_occurrence = -1
        while curr.next:
            maxima = prev.val < curr.val > curr.next.val
            minima = prev.val > curr.val < curr.next.val
            if maxima or minima:
                if last_occurrence == -1:
                    first_index = index
                else:
                    result[0] = min(result[0], index - last_occurrence)
                    result[1] = index - first_index
                last_occurrence = index
            prev = curr
            curr = curr.next  
            index += 1

        return [-1, -1] if result[-1] == -1 else result
