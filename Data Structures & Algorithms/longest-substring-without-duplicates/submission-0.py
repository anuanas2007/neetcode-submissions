class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        l = 0
        r = 0
        globalm = 1
        se = set()

        while r < len(s):
            while r < len(s) and s[r] not in se:
                se.add(s[r])
                globalm = max(globalm, r-l+1)
                r += 1
            
            while  r < len(s) and s[r] in se :
                se.remove(s[l])
                l += 1
            
        return globalm



        