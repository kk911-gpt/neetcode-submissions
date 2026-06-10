class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0
        lo=0
        hi= len(height)-1

        leftmax= height[lo]
        rightmax= height[hi]

        res=0

        while lo < hi:

            if leftmax< rightmax:
                lo+=1
                leftmax= max(leftmax, height[lo])
                res+= leftmax-height[lo]
            else:
                hi-=1
                rightmax= max(rightmax, height[hi])
                res+= rightmax-height[hi]
        return res
        