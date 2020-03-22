class Solution:
    def romanToInt(self, s: str) -> int:
        # first solution, fast and memory efficient
        roman_dict = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}
        num = 0
        digits = len(s)
        for i in range(digits):
            if s[i] in "IXC" and i < digits - 1:
                if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                    num -= roman_dict[s[i]]
                elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                    num -= roman_dict[s[i]]
                elif s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                    num -= roman_dict[s[i]]
                else:
                    num += roman_dict[s[i]]
            else:
                num += roman_dict[s[i]]
        return num


s = Solution()
roman = "MCMXCIV"
print(s.romanToInt(roman))