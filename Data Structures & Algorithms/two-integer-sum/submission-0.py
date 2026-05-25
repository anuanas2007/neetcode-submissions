class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i in range(len(nums)):
            lookup[nums[i]] = i
        
        for j in range(len(nums)):
            pair = target - nums[j]
            if pair in lookup:
                if lookup[pair] != j:
                    return [j, lookup[pair]]
