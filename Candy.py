class Solution:
    def candy(self, ratings) -> int:
        candies = [0 for i in range(len(ratings))]
        self.set_min(ratings, 0, len(ratings), candies)
        return sum(candies)

    def set_min(self, ratings, start, end, candies):
        if start >= end:
            return
        min_idx = ratings.index(min(ratings[start: end]), start, end)
        if min_idx == start or min_idx == end - 1:
            if min_idx == start:
                if start > 0 and ratings[min_idx] > ratings[min_idx - 1]:
                    candies[min_idx] = candies[min_idx - 1] + 1
                else:
                    candies[min_idx] = 1
            if min_idx == end - 1:
                if end < len(ratings) and ratings[min_idx] > ratings[min_idx + 1]:
                    candies[min_idx] = max(candies[min_idx + 1] + 1, candies[min_idx])
                else:
                    if candies[min_idx] == 0:
                        candies[min_idx] = 1
        else:
            candies[min_idx] = 1
        self.set_min(ratings, start, min_idx, candies)
        self.set_min(ratings, min_idx+1, end, candies)


s = Solution()
print(s.candy([3, 2, 1, 4, 3, 4, 5]))
