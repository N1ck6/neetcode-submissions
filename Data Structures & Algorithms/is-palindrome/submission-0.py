class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = [i.lower() for i in s if i.isalnum()]
        n = len(input)
        for i in range(len(input) // 2):
            if not input[i] == input[-i-1]: return False
        return True