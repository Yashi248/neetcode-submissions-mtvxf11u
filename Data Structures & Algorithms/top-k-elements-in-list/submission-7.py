class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        f = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n,0)+1
        
        for n,c in count.items():
            f[c].append(n)

        for j in range(len(f)-1,0,-1):
            res.extend(f[j])
            if len(res) == k:
                return res