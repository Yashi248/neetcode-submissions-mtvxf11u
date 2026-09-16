class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            al = [0]*26
            for i in s:
                al[ord(i)-ord('a')]+=1
            hashmap[tuple(al)].append(s)
        return list(hashmap.values())