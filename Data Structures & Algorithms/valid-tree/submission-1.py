class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        
        tree = [[] for _ in range(n)]

        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)

        q = deque()
        visit = set()

        q.append((0, -1))

        while q:
            cur, par = q.popleft()

            if cur in visit:
                return False
            
            visit.add(cur)
            
            for ed in tree[cur]:
                if ed != par:
                    q.append((ed, cur))
        
        return len(visit) == n


        