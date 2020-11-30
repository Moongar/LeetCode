from collections import deque


class Solution:
    def canReach(self, arr, start: int) -> bool:
        visit = deque([start])
        visited = {}
        return self.bfs(arr, visited, visit)

    def bfs(self, arr, visited, visit):
        if not visit:
            return False
        pos = visit.popleft()
        if arr[pos] == 0:
            return True
        visited[pos] = True
        if pos - arr[pos] >= 0 and pos - arr[pos] not in visited:
            visit.append(pos - arr[pos])
        if pos + arr[pos] < len(arr) and pos + arr[pos] not in visited:
            visit.append(pos + arr[pos])
        return self.bfs(arr, visited, visit)


s = Solution()
print(s.canReach([3,0,2,1,2], 1))
