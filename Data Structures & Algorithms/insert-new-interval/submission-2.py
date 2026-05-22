class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        i = 0
        n = len(intervals)

        # add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # merge overlaps
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        # add remaining
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
        # class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         s = newInterval[0]
#         e = newInterval[1]

#         i = 0
#         while i < len(intervals) and intervals[i][1] < s:
#             i += 1

#         if i >= len(intervals):
#             intervals.append(newInterval)
#             return intervals

#         if intervals[i][0] > e:
#             return intervals[:i] + [newInterval] + intervals[i:]
        
#         ns = intervals[i][0]
#         ind = i
#         while i < len(intervals) and intervals[i][1] <= e:
#             intervals.pop(i)
#             i += 1
        
#         if i >= len(intervals):
#             intervals.append([ns, e])
#             return intervals
        
#         else:
#             if intervals[i][0] > e:
#                 return intervals[:i] + [ns, e] + intervals[i:]
#             else:
#                 intervals[i][0] = ns
#                 return intervals
        
#         return intervals

        

        