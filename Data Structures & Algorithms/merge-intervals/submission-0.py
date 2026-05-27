class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for s, e in intervals:
            le = res[-1][1]

            if s <= le:
                res[-1][1] = max(e, le)
            
            else:
                res.append([s,e])
        
        return res
            




        