class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in hashmap and i != hashmap.get(diff,0):
                return [hashmap[diff]+1,i+1]
            hashmap[numbers[i]] = i
        return []