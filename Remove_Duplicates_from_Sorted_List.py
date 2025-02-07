class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            # If the current node's value is the same as the next node's value, remove the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        return head
