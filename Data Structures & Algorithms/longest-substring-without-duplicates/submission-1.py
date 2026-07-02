class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        n = len(s)
        if n < 2: return n

        l, r = 0, 1
        chars = {s[l]: l}
        while r < n:
            if s[r] in chars and chars[s[r]] >= l:
                longest = max(longest, r-l)
                l = chars[s[r]] + 1
                chars[s[r]] = r
            else:
                chars[s[r]] = r
            r += 1
        longest = max(longest, r-l)
        return longest