class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr


        # res = 0
        # for i in range(len(nums)):
        #     res += i - nums[i]
        # res += len(nums)
        # return res
        