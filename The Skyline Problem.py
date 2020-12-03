class Solution:
    def getSkyline(self, buildings):
        res = []
        b = buildings[0]
        left, right, height = b

        for i in range(1, len(buildings)):
            b = buildings[i]
            if b[0] == left:
                right = b[1]
                height = b[2]


        return res


s = Solution()
print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
