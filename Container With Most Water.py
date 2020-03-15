def maxArea(height):
    # First solution, it works but exceeds the time limit. O(n^2)
    # max_area = 0
    # for idx in range(len(height)):
    #     for idx2 in range(idx+1, len(height)):
    #         min_height = min(height[idx], height[idx2])
    #         area = min_height * (idx2 - idx)
    #         if area > max_area:
    #             max_area = area
    # second solution: start from the end and find the farthest container with the same height
    # faster, but still too slow to get accepted
    max_area = 0
    idx1 = 0
    idx2 = len(height) - 1
    while idx1 < len(height) - 1:
        area = min(height[idx1], height[idx2]) * (idx2 - idx1)
        if area > max_area:
            max_area = area
        if height[idx2] >= height[idx1] or idx1 == (idx2 - 1) or max_area > height[idx1] * (idx2 - idx1 - 1):
            idx1 += 1
            idx2 = len(height) - 1
        else:
            idx2 -= 1

    return max_area


height = [1, 8, 6, 2, 5, 4, 5, 3, 8, 7]
print(maxArea(height))