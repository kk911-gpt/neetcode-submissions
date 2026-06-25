class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #distinct_numbers=set(nums)
        #number = 2*sum(distinct_numbers) - sum(nums)
        #return number

        a=0

        for x in nums:
            a ^= x
        return a
