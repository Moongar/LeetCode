class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) < 11:
            return []
        seq = []
        for i in range(len(s) - 10):
            candid = s[i: i+10]
            sec = i + 1
            while sec <= len(s) - 10:
                if candid == s[sec: sec + 10]:
                    seq.append(candid)
                sec += 1
        return set(seq)


st = "AAAAAAAAAAA"
sol = Solution()
print(sol.findRepeatedDnaSequences(st))
