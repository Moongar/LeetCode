def removeDuplicates(nums):
    #solution 1 O(n)
    count = 0
    my_dict = {}
    for n in nums:
        if n not in my_dict.keys():
            my_dict[n] = 1
            nums[count] = n
            count += 1

    return count


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
print(nums)