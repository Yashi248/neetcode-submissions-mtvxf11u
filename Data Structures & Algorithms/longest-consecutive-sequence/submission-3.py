class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        max_len = 0

        for x in new:
            if x-1 not in new:
                cur_len = 1
                while(x + cur_len) in new:
                    cur_len +=1
                max_len = max(max_len, cur_len)
        return max_len

                




            