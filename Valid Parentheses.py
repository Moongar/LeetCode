class Solution:
    def isValid(self, s: str) -> bool:
        # first solution, fast and memory efficient O(n)
        opens = []
        for c in s:
            if c == ")":
                if len(opens) > 0 and opens[-1] == "(":
                    opens.pop()
                else:
                    return False
            elif c == "]":
                if len(opens) > 0 and opens[-1] == "[":
                    opens.pop()
                else:
                    return False
            elif c == "}":
                if len(opens) > 0 and opens[-1] == "{":
                    opens.pop()
                else:
                    return False
            else:
                opens.append(c)
        if len(opens) != 0:
            return False
        return True


s = Solution()
print(s.isValid("[{({})}]{()}"))

