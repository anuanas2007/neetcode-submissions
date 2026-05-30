class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        def caneat(n):
            time = 0
            for p in piles:
                time += math.ceil(p/n)
            if time <= h:
                return True
            else:
                return False
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = l + (r-l)//2
            if caneat(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
        