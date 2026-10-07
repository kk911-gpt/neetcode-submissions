class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def backtrack(current,used):
            if len(current)==len(nums):
                result.append(current.copy())
                return 
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                current.append(nums[i])
                used[i]=True

                backtrack(current,used)

                used[i]=False
                current.pop()
        backtrack([], [False]*len(nums))
        return result