class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lower_bound():
            low, high = 0, len(nums) - 1
            ans = len(nums)

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ans

        def upper_bound():
            low, high = 0, len(nums) - 1
            ans = len(nums)

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ans

        left = lower_bound()

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = upper_bound() - 1

        return [left, right]