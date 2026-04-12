class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap and i != hashmap[diff]:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
        return []
