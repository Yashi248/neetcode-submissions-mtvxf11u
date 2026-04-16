class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        win_map, t_map = {},{}
        for c in t:
            t_map[c] = t_map.get(c,0) + 1
        
        have, need = 0, len(t_map)
        res,resLen = [-1,-1], float('infinity')
        l=0
        for r in range(len(s)):
            win_map[s[r]] = win_map.get(s[r],0) + 1

            if s[r] in t_map and win_map[s[r]] == t_map[s[r]]:
                have+=1
            
            while have ==need:
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                win_map[s[l]] -=1
                if s[l] in t_map and win_map[s[l]] < t_map[s[l]]:
                    have-=1 
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ""
            



        
