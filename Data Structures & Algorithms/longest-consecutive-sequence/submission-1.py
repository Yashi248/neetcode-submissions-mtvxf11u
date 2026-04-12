class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        new = list(set(nums))
        new.sort()

        cur_len = 1
        max_len = 1
        for i in range(1,len(new)):
            if new[i] - new[i-1] == 1:
                cur_len +=1
                max_len = max(max_len, cur_len)
            elif new[i] != new[i-1]:
                cur_len = 1
        return max_len


            