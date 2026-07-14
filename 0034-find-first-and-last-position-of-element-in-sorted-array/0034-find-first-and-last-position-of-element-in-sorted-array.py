class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_target(start, end):
            if start > end:
                return [-1, -1]

            middle = (start + end) // 2

            if nums[middle] == target:
                left = middle
                right = middle

                while left - 1 >= 0 and nums[left - 1] == target:
                    left -= 1

                while right + 1 < len(nums) and nums[right + 1] == target:
                    right += 1

                return [left, right]

            elif nums[middle] < target:
                return find_target(middle + 1, end)

            else:
                return find_target(start, middle - 1)

        if not nums:
            return [-1, -1]

        return find_target(0, len(nums) - 1)