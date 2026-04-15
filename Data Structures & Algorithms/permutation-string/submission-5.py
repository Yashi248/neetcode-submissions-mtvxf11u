class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr_s1 = 26 * [0]
        for s in s1:
            arr_s1[ord(s)-ord('a')] +=1
        
        l, r = 0, len(s1)-1
        while r < len(s2):
            arr_s2 = 26* [0]
            for i in range(l,r+1):
                arr_s2[ord(s2[i])-ord('a')] +=1
            if arr_s1 == arr_s2:
                return True
            else:
                arr_s2[ord(s2[l])-ord('a')] -=1
                l+=1
                r+=1
        return False


