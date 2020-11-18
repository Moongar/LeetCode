class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            i += 1
            while i < len(intervals) and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                i += 1
            merged.append([start, end])

        return merged


s = Solution()
print(s.merge([[2, 6], [1, 3], [8, 10], [7, 18]]))
