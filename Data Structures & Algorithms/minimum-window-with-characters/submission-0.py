class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        tcount = {}
        scount = {}
        for i in range(len(t)):
            tcount[t[i]] = tcount.get(t[i],0) + 1

        min_len = float("infinity")
        res = [-1,-1]
        l=0
        have, need = 0,len(tcount)

        for r in range(len(s)):
            scount[s[r]] = scount.get(s[r],0) + 1
            if s[r] in tcount and scount[s[r]] == tcount[s[r]]:
                have+=1
            while have == need:
                cur_len = r-l+1
                if cur_len < min_len:
                    min_len = cur_len
                    res = [l,r]
                scount[s[l]] -=1
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if min_len != float("infinity") else ""    








