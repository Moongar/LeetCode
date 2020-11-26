class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        longest = 0
        for i in range(len(s)):
            letters = {s[i]: 1}
            if self.at_least_k(letters, k):
                longest = max(longest, sum(letters.values()))
            for j in range(i+1, len(s)):
                if s[j] in letters:
                    letters[s[j]] += 1
                else:
                    letters[s[j]] = 1
                if self.at_least_k(letters, k):
                    longest = max(longest, sum(letters.values()))
        return longest

    def at_least_k(self, letters, k):
        return all(v >= k for v in letters.values())


s = Solution()
print(s.longestSubstring("abcdabbc", 2))
