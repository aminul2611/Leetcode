class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        tail.next = head

        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
    
def build_linked_list(arr):
        dummy = ListNode(0)
        cur = dummy
        for x in arr:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next
    
def to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

