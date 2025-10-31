class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counted = set()
        x = 0
        while x < len(nums):
            element = nums[x]
            if element in counted:        # ✅ Skip if we already counted this
                x += 1
                continue
            counted.add(element)

            count = 0
            for key in nums:
                if key == element:
                    count += 1
                    if count > len(nums) / 2:
                        return element
            x += 1
