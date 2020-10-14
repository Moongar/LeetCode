class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            count = {}
            for c in A:
                if c in count:
                    return True
                else:
                    count[c] = True
            return False
        first = False
        for i in range(len(A)):
            if first and A[i] != B[i]:
                if A[i] == B[i1] and A[i1] == B[i]:
                    if A[i+1:] == B[i+1:]:
                        return True
                return False
            if not first and A[i] != B[i]:
                first = True
                i1 = i
        return not first


str1 = "aa"
str2 = "aa"
s = Solution()
print(s.buddyStrings(str1, str2))
