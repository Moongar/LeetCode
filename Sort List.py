# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        head = ListNode(arr[0])
        current = head
        for n in arr[1:]:
            next_node = ListNode(n)
            current.next = next_node
            current = current.next
        return head
