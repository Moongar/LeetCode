class Solution:
    def bagOfTokensScore(self, tokens, P: int) -> int:
        tokens.sort()
        if len(tokens) < 1:
            return 0
        score = 0
        left, right = 0, len(tokens) - 1
        while P >= 0 and left <= right:
            if P >= tokens[left]:
                score += 1
                P -= tokens[left]
                left += 1
            else:
                if score > 0 and tokens[right] > tokens[left]:
                    score -= 1
                    P += tokens[right]
                    right -= 1
                else:
                    break
        return score


s = Solution()
tokens = [33, 41, 10, 91, 47, 84, 98, 34, 48, 70]
p = 43
print(s.bagOfTokensScore(tokens, p))
