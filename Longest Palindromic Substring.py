class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    if j-i > len(longest):
                        longest = s[i:j]
        return longest


sol = Solution()
print(sol.longestPalindrome("abbas"))
