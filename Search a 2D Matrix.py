class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        target_row = self.find_row(matrix, target)
        return self.find_elem(matrix[target_row], target)

    def find_elem(self, row, target):
        left = 0
        right = len(row) - 1
        if len(row) == 1:
            return row[0] == target
        if row[left] == target or row[right] == target:
            return True
        if row[left] > target or row[right] < target:
            return False
        while right > left:
            mid = (left + right) // 2
            if mid == left or mid == right:
                break
            if target == row[mid]:
                return True
            elif target > row[mid]:
                left = mid
            else:
                right = mid
        return row[mid] == target

    def find_row(self, matrix, target):
        if len(matrix) == 1:
            return 0
        top_row = 0
        if matrix[top_row][-1] >= target:
            return top_row
        bot_row = len(matrix) - 1
        if matrix[bot_row - 1][-1] < target:
            return bot_row
        while bot_row > top_row:
            mid_row = (top_row + bot_row) // 2
            if mid_row == top_row or mid_row == bot_row:
                break
            if target > matrix[mid_row][-1]:
                top_row = mid_row
            else:
                if target < matrix[mid_row][0]:
                    bot_row = mid_row
                else:
                    return mid_row
        return mid_row


s = Solution()
mat = [[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]]
print(s.searchMatrix(mat, -5))
