class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        f = [[] for a in range(len(nums)+1)]

        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for c, v in count.items():
            f[v].append(c)
        
        for j in range(len(f)-1,0,-1):
            for n in f[j]:
                res.append(n)
                if len(res) == k:
                    return res