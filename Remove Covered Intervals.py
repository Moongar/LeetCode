class Solution:
    def removeCoveredIntervals(self, intervals):
        count = 0
        my_dict = {}
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    if j not in my_dict:
                        count += 1
                        my_dict[j] = True
                elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    if i not in my_dict:
                        count += 1
                        my_dict[i] = True
        return len(intervals) - count


s = Solution()
print(s.removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]))
