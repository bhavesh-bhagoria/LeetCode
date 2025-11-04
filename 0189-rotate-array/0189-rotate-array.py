class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # in case k > n
        nums[:] = nums[-k:] + nums[:-k]  # modify in-place
