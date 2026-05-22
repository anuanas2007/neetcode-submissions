class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        s = newInterval[0]
        e = newInterval[1]

        i = 0
        res = []

        # add intervals before overlap
        while i < len(intervals) and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1

        # merge overlapping intervals
        ns = s
        ne = e

        while i < len(intervals) and intervals[i][0] <= ne:
            ns = min(ns, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i += 1

        res.append([ns, ne])

        # add remaining intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res