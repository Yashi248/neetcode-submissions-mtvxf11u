class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        med = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for x, v in count.items():
            med[v].append(x)
        
        for j in range(len(med)-1,-1,-1):
            for l in med[j]:
                res.append(l)
                if len(res)==k:
                    return res