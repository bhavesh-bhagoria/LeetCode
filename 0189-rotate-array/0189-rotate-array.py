class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if k > len(nums):
            k = k % len(nums)
        if k == 0:
            return nums
        print(nums[-k:])
        print(nums[:len(nums)-k])
        nums[:] = nums[-k:] + nums[:len(nums)-k]

        
        
        