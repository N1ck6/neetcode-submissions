class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for each in strs:
            encoded.append(f"{len(each)}#{each}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            idx = s.index('#', i)
            num = int(s[i:idx])
            string = s[idx+1:idx+1+num]
            decoded.append(string)
            i = idx + 1 + num
        return decoded