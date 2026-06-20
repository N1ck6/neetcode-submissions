class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            a = nums.index(i)
            if nums[a + 1:].count(target - i) >= 1:
                return [a, nums[a + 1:].index(target - i) + a + 1]