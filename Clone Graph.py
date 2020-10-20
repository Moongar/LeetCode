# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {node: Node(node.val)}
        self.dfs(node, visited)
        return visited[node]

    def dfs(self, node, visited):
        for neigh in node.neighbors:
            if neigh not in visited:
                visited[neigh] = Node(neigh.val)
                self.dfs(neigh, visited)
            visited[node].neighbors.append(visited[neigh])


s = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node3]
node4.neighbors = [node2, node3]
node2.neighbors = [node1, node4]
node3.neighbors = [node1, node4]
print(s.cloneGraph(node1))
