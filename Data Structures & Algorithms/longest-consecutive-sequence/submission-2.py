class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # mp = defaultdict(int)
        # res = 0

        # for i in nums:
        #     if not mp[i]:
        #         mp[i] = mp[i-1] + mp[i+1] + 1
        #         mp[i - mp[i-1]] = mp[i]
        #         mp[i + mp[i+1]] = mp[i]
        #         res = max(res, mp[i])
        
        # return res

        numSet = set(nums)
        longest = 0

        for i in nums:
            # check if i is a starting number
            if (i - 1) not in numSet:
                length = 0
                while (i + length) in numSet:
                    length += 1
                
                longest = max(length, longest)
        
        return longest
        