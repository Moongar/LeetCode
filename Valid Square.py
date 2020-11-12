class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        p = [p1, p2, p3, p4]
        # pick p1 and find the other diagonal element
        dis = set([])
        for i in range(3):
            for j in range(i+1, 4):
                if p[i] == p[j]:
                    return False
                dis.add((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2)
        return len(dis) == 2


s = Solution()
print(s.validSquare([0, 0], [1, 1], [1, 0], [0, 1]))
# print(s.validSquare([0, 1], [1, 0], [-1, 0], [0, -1]))
# print(s.validSquare([1134,-2539], [492,-1255], [-792,-1897], [-150,-3181]))

