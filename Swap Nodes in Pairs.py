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
        if not head or not head.next:
            return head
        # first solution. slow and not memory efficient
        # temp1 = copy.deepcopy(head)
        # temp2 = copy.deepcopy(head.next)
        # head = head.next
        # head.next = temp1
        # tail = head.next
        # tail.next = temp2.next
        # while tail.next and tail.next.next:
        #     temp1 = copy.deepcopy(tail.next)
        #     temp2 = copy.deepcopy(tail.next.next)
        #     tail.next = tail.next.next
        #     tail = tail.next
        #     tail.next = temp1
        #     tail = tail.next
        #     tail.next = temp2.next

        # second solution using only one temp var. faster, but still slow and not memory efficient
        # temp = copy.deepcopy(head)
        # head = head.next
        # temp.next = head.next
        # head.next = temp
        # head2 = head
        # head2 = head2.next
        # while head2.next and head2.next.next:
        #     temp = copy.deepcopy(head2.next)
        #     head2.next = head2.next.next
        #     head2 = head2.next
        #     temp.next = head2.next
        #     head2.next = temp
        #     head2 = head2.next

        # third solution
        swap = ListNode(None)
        new = swap
        while head and head.next:
            temp1 = head
            temp2 = head.next
            temp3 = head.next.next
            new = temp2
            new.next = temp1
            new.next.next = temp3
            new = new.next.next
            head = head.next.next


        return swap


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