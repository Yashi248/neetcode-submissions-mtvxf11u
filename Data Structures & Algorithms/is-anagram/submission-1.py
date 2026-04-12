class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}

        for i in range(0,len(s)):
            map1[s[i]] = map1.get(s[i],0) + 1
            map2[t[i]] = map2.get(t[i],0) + 1
        
        for c in map1:
            if map1[c] != map2.get(c,0):
                return False
        return True