class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, result = 0, len(height) - 1, 0
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                result += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                result += rmax - height[r]

        return result