class Solution:
    def longestPalindrome(self, s: str) -> str:
        # naive O(n^3)
        # longest = ""
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         temp = s[i:j]
        #         if temp == temp[::-1]:
        #             if j-i > len(longest):
        #                 longest = s[i:j]
        # return longest
        if len(s) < 1:
            return ""
        left, right = 0, 0
        for i in range(len(s) - 1):
            l1, r1 = self.expand(i, i, s)
            l2, r2 = self.expand(i, i+1, s)
            if r1 - l1 >= r2 - l2 and r1 - l1 > right - left:
                left, right = l1, r1
            elif r1 - l1 < r2 - l2 and r2 - l2 > right - left:
                left, right = l2, r2

        return s[left:right + 1]

    def expand(self, l, r, s):
        if s[l] == s[r]:
            while l > 0 and r < len(s)-1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
        else:
            r = l
        return l, r





sol = Solution()
print(sol.longestPalindrome("bsaasb"))
