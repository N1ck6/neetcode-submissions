class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2: return False
        count_nums = {}
        for num in nums:
            if num in count_nums.keys(): return True
            count_nums[num] = ""
        return False