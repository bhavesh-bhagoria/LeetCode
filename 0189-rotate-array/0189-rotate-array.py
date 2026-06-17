class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        k = k % len(nums)
        while k < len(nums):
            temp.append(nums.pop(0))
        nums.extend(temp)