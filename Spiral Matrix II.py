class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        k = n
        arr = [[0 for _ in range(n)] for _ in range(n)]
        cur = 1
        row = 0
        col = 0
        while True:
            row, col, k, cur = self.go_right(arr, row, col, k, cur)
            if k == 0:
                break
            row, col, k, cur = self.go_down(arr, row, col, k, cur)
            row, col, k, cur = self.go_left(arr, row, col, k, cur)
            if k == 0:
                break
            row, col, k, cur = self.go_up(arr, row, col, k, cur)
        return arr

    def go_right(self, arr, row, col, k, cur):
        for i in range(k):
            arr[row][col + i] = cur
            cur += 1
        return row + 1, col + k - 1, k - 1, cur

    def go_down(self, arr, row, col, k, cur):
        for i in range(k):
            arr[row + i][col] = cur
            cur += 1
        return row + k - 1, col - 1, k, cur

    def go_left(self, arr, row, col, k, cur):
        for i in range(k):
            arr[row][col - i] = cur
            cur += 1
        return row - 1, col - k + 1, k - 1, cur

    def go_up(self, arr, row, col, k, cur):
        for i in range(k):
            arr[row - i][col] = cur
            cur += 1
        return row - k + 1, col + 1, k, cur
