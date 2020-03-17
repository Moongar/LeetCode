class Solution:
    # first solution O(n^2)
    def rotate(self, matrix) -> None:
        n = len(matrix) - 1
        for i in range((n+1) // 2):
            for j in range(i, n - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = temp
        pass


# mat = [
#   [1, 1, 1, 1, 1],
#   [2, 1, 1, 1, 3],
#   [2, 2, 0, 3, 3],
#   [2, 4, 4, 4, 3],
#   [4, 4, 4, 4, 4]
# ]

mat = [[2,29,20,26,16,28],
       [12,27,9,25,13,21],
       [32,33,32,2,28,14],
       [13,14,32,27,22,26],
       [33,1,20,7,21,7],
       [4,24,1,6,32,34]]

s = Solution()
s.rotate(mat)
for row in mat:
    print(row)