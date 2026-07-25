class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n

        # Step 1: Calculate left (prefix) products for each element
        # output[i] will store the product of all elements before index i
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        # Step 2: Calculate right (suffix) products and multiply with left products
        # We traverse from right to left, keeping track of the running right product
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output