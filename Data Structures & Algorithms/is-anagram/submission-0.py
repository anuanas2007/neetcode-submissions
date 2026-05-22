class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dicta = defaultdict(int)
        dictb = defaultdict(int)

        for i in range(len(s)):
            dicta[s[i]] += 1
            dictb[t[i]] += 1
        
        for k,v in dicta.items():
            if k not in dictb:
                return False
            if dictb[k] != v:
                return False
        
        return True


        