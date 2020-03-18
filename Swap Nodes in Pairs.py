# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.


import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        nums = self
        while nums is not None:
            print(nums.val, end =" ")
            nums = nums.next
        print("")
        pass


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # first solution. slow and not memory efficient
        if not head or not head.next:
            return head
        temp1 = copy.deepcopy(head)
        temp2 = copy.deepcopy(head.next)
        head = head.next
        head.next = temp1
        tail = head.next
        tail.next = temp2.next
        while tail.next and tail.next.next:
            temp1 = copy.deepcopy(tail.next)
            temp2 = copy.deepcopy(tail.next.next)
            tail.next = tail.next.next
            tail = tail.next
            tail.next = temp1
            tail = tail.next
            tail.next = temp2.next
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
head.print_list()
s.swapPairs(head).print_list()