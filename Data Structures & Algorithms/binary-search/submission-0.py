class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        if target < nums[mid]:
            for i in range(mid):
                if target == nums[i]:
                    return i
        elif target >= nums[mid]:
            for i in range(mid,len(nums)):
                if target == nums[i]:
                    return i
        return -1
        