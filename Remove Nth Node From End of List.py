# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def convert_to_num(self):
        nums = self
        num = 0
        while nums is not None:
            num = num * 10 + nums.val
            nums = nums.next
        return num

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # first solution using two pointers. very memory efficient but not fast
        l2 = head
        for iter in range(n):
            l2 = l2.next
        if not l2:
            return head.next
        else:
            l1 = head
            while l2.next:
                l1 = l1.next
                l2 = l2.next
            l1.next = l1.next.next
        return head


s= Solution()
head = ListNode(1)
nums = head
nums.next = ListNode(2)
nums = nums.next
nums.next = ListNode(3)
nums = nums.next
nums.next = ListNode(4)
nums = nums.next
nums.next = ListNode(5)
nums = nums.next
print(head.convert_to_num())
print(s.removeNthFromEnd(head, 4).convert_to_num())