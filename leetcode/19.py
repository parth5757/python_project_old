from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        
        idx_to_remove = length - n
        prev = None
        curr = head
        i = 0
        while curr is not None:
            if i == idx_to_remove:
                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            i += 1
        
        return head

p = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
q = p.removeNthFromEnd(head, n)
while q is not None:
    print(q.val)
    q = q.next
