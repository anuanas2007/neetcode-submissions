class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        preve = float("-inf")
        res = 0

        for s,e in intervals:
            if s < preve:
                if e > preve:
                    continue
    
            else:
                res += 1
            
            preve = e
        
        return len(intervals)- res


        