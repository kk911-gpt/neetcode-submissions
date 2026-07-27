class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, subset):
            # Every subset we create is a valid answer
            result.append(subset.copy())

            # Try adding each remaining number
            for i in range(index, len(nums)):
                subset.append(nums[i])

                backtrack(i + 1, subset)

                # Remove the number to try another possibility
                subset.pop()

        backtrack(0, [])

        return result