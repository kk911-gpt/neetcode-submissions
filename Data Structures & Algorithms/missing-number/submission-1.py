class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #res= len(nums)

        #for i in range (len(nums)):
           # res ^= i ^ nums[i]

        #return res

        n= len(nums)
        x1 = 0
        for i in range(n + 1):
            x1 ^= i

        x2 = 0
        for num in nums:
            x2 ^= num

        return x1 ^ x2
        

