def combinationSum(candidates, target):
    combs = []
    backtrack(candidates, target, [], combs)
    return combs


def backtrack(nums, target, path, combs):
    if target < 0:
        return
    if target == 0:
        combs.append(path)
        return
    for i in range(len(nums)):
        backtrack(nums[i:], target - nums[i], path + [nums[i]], combs)


cands = [2, 3, 5]
tar = 8
print(combinationSum(cands, tar))
