def mergeTwoLists(l1, l2):
    merged_list = []
    l1_idx = 0
    l2_idx = 0
    while l1_idx < len(l1) or l2_idx < len(l2):
        if l1_idx == len(l1):
            merged_list.append(l2[l2_idx])
            l2_idx += 1
        elif l2_idx == len(l2):
            merged_list.append(l1[l1_idx])
            l1_idx += 1
        else:
            if l1[l1_idx] < l2[l2_idx]:
                merged_list.append(l1[l1_idx])
                l1_idx += 1
            else:
                merged_list.append(l2[l2_idx])
                l2_idx += 1
    return merged_list


l1 = [1, 3, 4, 5, 6, 6, 6]
l2 = [1, 1, 1, 1, 2, 4]
print(mergeTwoLists(l1, l2))