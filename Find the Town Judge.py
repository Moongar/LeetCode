class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N == 1:
            return 1
        trust_dict = {}
        truster = {}
        for t in trust:
            if t[0] not in truster:
                truster[t[0]] = True
            if t[1] not in trust_dict:
                trust_dict[t[1]] = [t[0]]
            else:
                trust_dict[t[1]].append(t[0])
        for t in trust:
            if len(trust_dict[t[1]]) == N-1 and t[1] not in truster:
                return t[1]
        return -1


s = Solution()
print(s.findJudge(3, [[1,3],[2,3],[3,1]]))
