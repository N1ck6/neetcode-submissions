class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_dicts = []
        for s in strs:
            letters = {}
            for i in range(len(s)):
                if s[i] in letters:
                    letters[s[i]] += 1
                else:
                    letters[s[i]] = 1
            dict_dicts.append(letters)
        
        n = len(dict_dicts)
        otv = []
        while len(strs):
            a = []
            b = []
            for j in range(len(strs)):
                if dict_dicts[0] == dict_dicts[j]:
                    a.append(j)
                    b.append(strs[j])
            for ind in sorted(a, reverse=True):
                strs.pop(ind)
                dict_dicts.pop(ind)
            otv.append(b)
        return otv