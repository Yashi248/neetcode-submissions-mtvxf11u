class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i,j = 0, len(heights)-1
        while i<j:
            area = (j-i) * min(heights[i],heights[j])
            maxArea = max(maxArea, area)
            if i<j and heights[i] <= heights[j]:
                i+=1
            elif i<j and heights[i] > heights[j]:
                j-=1

        return maxArea