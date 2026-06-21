class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    result.append([nums[l], nums[i], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return result
