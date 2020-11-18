class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        loc = [0, 0]
        targets = [[p, 0], [p, p], [0, p]]
        hit_target = False
        up = True
        while not hit_target:
            loc[0] = (loc[0] + p) % (2 * p)
            if up:
                loc[1] += q
                if loc[1] > p:
                    loc[1] = p - (loc[1] - p)
                    up = False
            else:
                loc[1] -= q
                if loc[1] < 0:
                    loc[1] = - loc[1]
                    up = True
            if loc in targets:
                hit_target = True
                return targets.index(loc)


s = Solution()
print(s.mirrorReflection(2, 2/3))
