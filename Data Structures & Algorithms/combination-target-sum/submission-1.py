class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]

        def backtrack(start, remaining, current):
            if remaining== 0:
                result.append(current.copy())
                return result
            
            if remaining<0:
                return
            
            for i in range(start, len(nums)):
                current.append(nums[i])

                backtrack(i, remaining-nums[i],current)

                current.pop()
        backtrack(0,target,[])
        return result

