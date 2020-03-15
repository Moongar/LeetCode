def maxArea(height):
    # First solution, it works but exceeds the time limit. O(n^2)
    max_area = 0
    for idx in range(len(height)):
        for idx2 in range(idx+1, len(height)):
            min_height = min(height[idx], height[idx2])
            area = min_height * (idx2 - idx)
            if area > max_area:
                max_area = area

    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))