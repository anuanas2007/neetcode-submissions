"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        new = {}
        new[node] = Node(node.val)
        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()
            for ne in cur.neighbors:
                if ne not in new:
                    new[ne] = Node(ne.val)
                    q.append(ne)
                new[cur].neighbors.append(new[ne])

        return new[node]
        