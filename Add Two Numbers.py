# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def convert_to_num(self):
        nums = self
        num = 0
        pow = 0
        while nums is not None:
            num += nums.val * 10**pow
            nums = nums.next
            pow += 1
        return num


class Solution:
    def addTwoNumbers(self, l1 : ListNode, l2 : ListNode):
        add = l1.convert_to_num() + l2.convert_to_num()
        add_array = [0]
        while add > 0:
            add_array.append(add - (add // 10) * 10)
            add = add // 10
        # making the linked list
        add_linked_list = ListNode(add_array[0])
        res = add_linked_list
        for idx in range(1,len(add_array)):
            res.next = ListNode(add_array[idx])
            res = res.next
        return add_linked_list




s= Solution()
list1 = ListNode(2)
nums = list1
nums.next = ListNode(4)
nums = nums.next
nums.next = ListNode(3)
nums = nums.next
list2 = ListNode(5)
nums = list2
nums.next = ListNode(6)
nums = nums.next
nums.next = ListNode(4)
nums = nums.next
nums.next = ListNode(1)
nums = nums.next
print(list1.convert_to_num())
print(list2.convert_to_num())
print(s.addTwoNumbers(list1, list2).convert_to_num())
