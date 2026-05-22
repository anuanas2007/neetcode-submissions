class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)

        for a,b in prerequisites:
            prereq[a].append(b)
        
        done = set()

        def dfs(c):
            if c in done:
                return False
            
            if prereq[c] == []:
                return True
            
            done.add(c)

            for cr in prereq[c]:
                if not dfs(cr):
                    return False
            
            done.remove(c)
            prereq[c] = []
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
