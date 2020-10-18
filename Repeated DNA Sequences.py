class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) < 11:
            return []
        # first solution, brute force O(n^2) time
        # seq = []
        # for i in range(len(s) - 10):
        #     candid = s[i: i+10]
        #     sec = i + 1
        #     while sec <= len(s) - 10:
        #         if candid == s[sec: sec + 10]:
        #             seq.append(candid)
        #             break
        #         sec += 1
        # second solution using a hash table, O(n) time, O(n) memory
        seq = []
        diction = {}
        for i in range(len(s) - 9):
            if s[i: i + 10] in diction:
                diction[s[i: i + 10]] += 1
                if diction[s[i: i + 10]] == 2:
                    seq.append(s[i: i + 10])
            else:
                diction[s[i: i + 10]] = 1
        return seq


st = "AAAAAAAAAAABBAAAAAAAAAB"
sol = Solution()
print(sol.findRepeatedDnaSequences(st))
