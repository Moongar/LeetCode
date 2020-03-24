class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # first solution, memory efficient but very slow
        if len(s) < 1:
            return 0
        longest = 1
        start_idx = 0
        seen = {s[0]: True}
        while start_idx < len(s) - 1:
            seen = {s[start_idx]: True}
            current_len = 1
            end_idx = start_idx + 1
            while s[end_idx] not in seen.keys():
                seen[s[end_idx]] = True
                current_len += 1
                end_idx += 1
                if end_idx == len(s):
                    return max(current_len, longest)
            longest = max(current_len, longest)
            start_idx += 1
        return longest


input_s = "wew"
s = Solution()
print(s.lengthOfLongestSubstring(input_s))
