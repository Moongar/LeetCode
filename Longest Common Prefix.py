class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        common = ""
        first = strs.pop()
        for idx in range(len(first)):
            for word in strs:
                if len(word) <= idx or word[idx] != first[idx]:
                    return common
            common += first[idx]

        return common


s = Solution()
arr = ["car","car","car","cart",""]
print(s.longestCommonPrefix(arr))