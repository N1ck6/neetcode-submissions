class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 2: 
            return 0

        pr = [0] * n
        suff = [0] * n

        mx = 0
        for i in range(1, n):
            mx = max(mx, height[i-1])
            pr[i] = mx

        mx = 0
        for i in range(n-2, -1, -1):
            mx = max(mx, height[i + 1])
            suff[i] = mx
        
        result = 0
        for i in range(n):
            result += max(0, min(pr[i], suff[i]) - height[i])

        return result