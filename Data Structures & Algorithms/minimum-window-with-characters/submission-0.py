class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        cntr = Counter(t)
        cur = defaultdict(int)
        need = len(cntr)
        have = 0

        l, r = 0, 0
        res = ""

        while r < len(s):
            if s[r] in cntr:
                cur[s[r]] += 1
                if cur[s[r]] == cntr[s[r]]:
                    have += 1 
                    while have == need:
                        if res == "" or len(res) > r-l+1:
                            res = s[l:r+1]
                        if s[l] in cntr:
                            cur[s[l]] -= 1
                            if cur[s[l]] < cntr[s[l]]:
                                have -= 1
                        l += 1
            
            r += 1

        return res


