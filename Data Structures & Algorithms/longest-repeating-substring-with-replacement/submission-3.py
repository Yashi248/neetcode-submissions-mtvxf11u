class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l=0
        res = 0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r],0) + 1
            win_len = r-l+1 
            if win_len - max(hashmap.values()) <= k:
                res = max(res,r-l+1)
                continue
            else:
                hashmap[s[l]] = hashmap.get(s[l],0) - 1
                l+=1
        return res

