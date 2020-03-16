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
    def addTwoNumbers(self, l1 : ListNode, l2 : ListNode) -> ListNode:
        # first solution, convert lists to numbers, convert the sum back to a linke list. too slow
        # add = l1.convert_to_num() + l2.convert_to_num()
        # add_array = [0]
        # while add > 0:
        #     add_array.append(add - (add // 10) * 10)
        #     add = add // 10
        # # making the linked list
        # add_linked_list = ListNode(add_array[0])
        # res = add_linked_list
        # for idx in range(1,len(add_array)):
        #     res.next = ListNode(add_array[idx])
        #     res = res.next
        # return add_linked_list

        # second solution: directly work with the linked lists
        # adding first numbers
        add_num = l1.val + l2.val
        if add_num >= 10:
            extra = 1
            add_num -= 10
        else:
            extra = 0
        sum_list = ListNode(add_num)
        res = sum_list
        l1 = l1.next
        l2 = l2.next
        # adding the rest of the numbers
        while l1 or l2:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            add_num = num1 + num2 + extra
            if add_num >= 10:
                extra = 1
                add_num -= 10
            else:
                extra = 0
            res. next = ListNode(add_num)
            res = res.next
        if extra > 0:
            res.next = ListNode(extra)
            res = res.next
        return sum_list




s= Solution()
list1 = ListNode(5)
# nums = list1
# nums.next = ListNode(4)
# nums = nums.next
# nums.next = ListNode(3)
# nums = nums.next
list2 = ListNode(5)
# nums = list2
# nums.next = ListNode(6)
# nums = nums.next
# nums.next = ListNode(4)
# nums = nums.next
print(list1.convert_to_num())
print(list2.convert_to_num())
print(s.addTwoNumbers(list1, list2).convert_to_num())
