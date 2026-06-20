class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        nums.sort()
        maxC, currC, lmin = 0, 0, nums[0] - 1
        for i in nums:
            if lmin + 1 == i:
                currC += 1
                lmin += 1
            elif lmin == i:
                continue
            else:
                maxC = max(maxC, currC)
                currC = 1
                lmin = i
        maxC = max(maxC, currC)
        return maxC