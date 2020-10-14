class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for c in sorted(set(s)):
            rest = s[s.index(c):]
            if set(rest) == set(s):
                return c + self.removeDuplicateLetters(rest.replace(c, ''))
        return ''


s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))
