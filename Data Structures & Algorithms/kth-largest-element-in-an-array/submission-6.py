class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k

        def quickStart(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: return quickStart(l,p-1)
            elif p < k: return quickStart(p+1,r)
            else: return nums[p]
        
        return quickStart(0,len(nums)-1)