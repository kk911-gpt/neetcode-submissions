class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)

        if n==1:
            return nums[0]
        def houserobber(arr):
            a= len(arr)

            if a==1:
                return arr[0]
            dp= [0]*a
            
            dp[0]= arr[0]
            dp[1]= max(arr[0], arr[1])

            for i in range(2,a):
                dp[i]= max(dp[i-1],dp[i-2]+arr[i])
            return dp[a-1]
        case1= houserobber(nums[:-1])
        case2= houserobber(nums[1:])
        return max(case1, case2)