class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        c = 1
        for i in range(n):
            result[i] = c
            c *= nums[i]
        
        c = 1
        for i in range(n-1, -1, -1):
            result[i] *= c
            c *= nums[i]
        return result