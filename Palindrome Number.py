class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        invert = 0
        while original > 0:
            invert = 10 * invert + original % 10
            original = original // 10
        if invert == x:
            return True
        return False


s = Solution()
print(s.isPalindrome(6))