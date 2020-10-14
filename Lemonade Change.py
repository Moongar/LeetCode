class Solution:
    def lemonadeChange(self, bills) -> bool:
        n5 = 0
        n10 = 0
        for n in bills:
            if n == 5:
                n5 += 1
            elif n == 10:
                if n5 > 0:
                    n10 += 1
                    n5 -= 1
                else:
                    return False
            else:
                if n10 > 0 and n5 > 0:
                    n5 -= 1
                    n10 -= 1
                elif n5 > 2:
                    n5 -= 3
                else:
                    return False
        return True


s = Solution()
print(s.lemonadeChange([5,5,10,10,20]))
