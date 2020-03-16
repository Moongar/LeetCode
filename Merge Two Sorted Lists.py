# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    # first solution for lists O(n)
    # merged_list = []
    # l1_idx = 0
    # l2_idx = 0
    # while l1_idx < len(l1) or l2_idx < len(l2):
    #     if l1_idx == len(l1):
    #         merged_list.append(l2[l2_idx])
    #         l2_idx += 1
    #     elif l2_idx == len(l2):
    #         merged_list.append(l1[l1_idx])
    #         l1_idx += 1
    #     else:
    #         if l1[l1_idx] < l2[l2_idx]:
    #             merged_list.append(l1[l1_idx])
    #             l1_idx += 1
    #         else:
    #             merged_list.append(l2[l2_idx])
    #             l2_idx += 1
    # return merged_list
    # second solution using singly linked lists O(n)
    if l1 == None and l2 == None:
        return None
    res = ListNode(None)
    merged_list = res
    first = True
    while l1 != None or l2 != None:
        if not first:
            merged_list.next = ListNode(None)
            merged_list = merged_list.next
        if l1 == None:
            merged_list.val = l2.val
            l2 = l2.next
        elif l2 == None:
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
