class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge = defaultdict(list)

        for a, b in edges:
            edge[a].append(b)
            edge[b].append(a)
        
        seen = set()
        res = 0

        def bfs(i):
            q = deque()
            q.append(i)

            while q:
                cur = q.popleft()
                seen.add(cur)

                for ed in edge[cur]:
                    if ed not in seen:
                        q.append(ed)

        for i in range(n):
            if i not in seen:
                bfs(i)
                res += 1

        return res      
        