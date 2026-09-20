class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l=0
        maxLen = 1
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxLen = max(maxLen,r-l+1)
        
        return maxLen

