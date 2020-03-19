class Solution:
    def isValidSudoku(self, board) -> bool:
        # first solution using 3 dictionaries. fast and memory efficient
        rows = {}
        cols = {}
        sqrs = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    # check row
                    if i*10 + int(board[i][j]) in rows.keys():
                        return False
                    else:
                        rows[i*10 + int(board[i][j])] = 1

                    # check column
                    if j*10 + int(board[i][j]) in cols.keys():
                        return False
                    else:
                        cols[j*10 + int(board[i][j])] = 1
                    #check square
                    if (i // 3) * 100 + (j // 3) * 10 + int(board[i][j]) in sqrs.keys():
                        return False
                    else:
                        sqrs[(i // 3) * 100 + (j // 3) * 10 + int(board[i][j])] = 1

        return True


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","5","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
s = Solution()
print(s.isValidSudoku(board))