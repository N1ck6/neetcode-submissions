class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx, result = 0, 0
        n = len(heights)

        for i in heights:
            if i > mx:
                mx = i
        
        for height in range(mx, -1, -1):
            start = next((x for x in range(n) if heights[x] >= height), None)
            end = next((x for x in range(n-1, -1, -1) if heights[x] >= height), None)

            if start != None and end != None:
                if height * (end - start) > result:
                    result = height * (end - start)
            
            if result > n * (height-1):
                break

        return result