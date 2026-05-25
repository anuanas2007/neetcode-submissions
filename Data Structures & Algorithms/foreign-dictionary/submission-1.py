class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dic = {}
        for word in words:
            for c in word:
                dic[c] = set()
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minl = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minl] == w2[:minl]:
                return ""
            for j in range(minl):
                if w1[j] != w2[j]:
                    dic[w1[j]].add(w2[j])
                    break
        res = []
        visited = {}

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True
            for nei in dic[char]:
                if dfs(nei):
                    return True
            res.append(char)
            visited[char] = False
            

        for c in dic:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)