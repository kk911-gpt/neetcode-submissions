class Solution:
    def maxArea(self, heights: List[int]) -> int:

        lo=0
        hi= len(heights)-1
        max_area= float ('-inf')

        while lo <hi:
            area= min(heights[lo], heights[hi]) * (hi-lo)
            max_area= max(max_area, area)

            if heights[lo]< heights[hi]:
                lo+=1
            else:
                hi-=1
        return max_area


        