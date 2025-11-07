class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Step 1: create output array filled with 1s

        # ----- Left Pass -----
        i = 0
        left_product = 1
        while i < n:
            answer[i] = left_product
            left_product *= nums[i]
            i += 1
        i = n - 1
        right_product = 1
        while i >= 0:
            answer[i] *= right_product
            right_product *= nums[i]
            i -= 1

        return answer
