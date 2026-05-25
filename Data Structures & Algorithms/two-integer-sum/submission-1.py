class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in lookup:
                return [lookup[pair], i]

            lookup[nums[i]] = i
        
