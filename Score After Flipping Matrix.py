class Solution:
    def matrixScore(self, A) -> int:
        res = 0
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[i])):
                    if A[i][j] == 0:
                        A[i][j] = 1
                    else:
                        A[i][j] = 0
        for j in range(len(A[0])):
            summ = 0
            for i in range(len(A)):
                summ += A[i][j]
            res = res * 2 + max(summ, len(A) - summ)
        return res


s = Solution()
print(s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
