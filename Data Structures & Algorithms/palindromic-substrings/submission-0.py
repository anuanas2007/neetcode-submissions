class Solution:
    def countSubstrings(self, s: str) -> int:

        def process(t):
            return "^#" + "#".join(t) + "#$"
            # res = "##"
            # for i in t:
            #     res += i + "#"
            # res += "#"
            # return res
        
        t = process(s)
        print(t)
        n = len(t)
        p = [0] * n

        center = 0
        right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])
            
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
            
            if i + p[i] > right:
                center = i
                right = i + p[i]
            
        ans = 0
        for v in p:
            ans += (v + 1) // 2

        return ans