class Solution:
    def combinationSum(self, nums, target):
        res = []

        def backtrack(i, curr, total):
            # Base case: target reached
            if total == target:
                res.append(curr.copy())
                return

            # Invalid case
            if i >= len(nums) or total > target:
                return

            # Choice 1: take nums[i]
            # Stay at i because we can reuse the same number
            curr.append(nums[i])
            backtrack(i, curr, total + nums[i])
            curr.pop()

            # Choice 2: skip nums[i]
            # Move to the next number
            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)
        return res