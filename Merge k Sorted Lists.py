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
    #first solution using a method for mwrging two lists. too slow
    def mergeTwoLists(selfself, l1, l2):
        if not l1 and not l2:
            return l1
        res = ListNode(None)
        merged_list = res
        first = True
        while l1 or l2:
            if not first:
                merged_list.next = ListNode(None)
                merged_list = merged_list.next
            if not l1:
                merged_list.val = l2.val
                l2 = l2.next
            elif not l2:
                merged_list.val = l1.val
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    merged_list.val = l1.val
                    l1 = l1.next
                else:
                    merged_list.val = l2.val
                    l2 = l2.next
            first = False

        return res
    def mergeKLists(self, lists) -> ListNode:
        if not len(lists):
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            l1 = lists.pop()
            while len(lists) > 0:
                l2 = lists.pop()
                l1 = self.mergeTwoLists(l1, l2)

        return l1


s= Solution()
head1 = ListNode(1)
nums = head1
nums.next = ListNode(2)
nums = nums.next
nums.next = ListNode(3)
nums = nums.next
nums.next = ListNode(4)
nums = nums.next
head2 = ListNode(1)
nums = head2
nums.next = ListNode(3)
nums = nums.next
nums.next = ListNode(5)
nums = nums.next
head3 = ListNode(1)
nums = head3
nums.next = ListNode(3)
nums = nums.next
nums.next = ListNode(6)
nums = nums.next
nums.next = ListNode(6)
nums = nums.next
head1.print_list()
head2.print_list()
s.mergeKLists([head1, head2, head3]).print_list()