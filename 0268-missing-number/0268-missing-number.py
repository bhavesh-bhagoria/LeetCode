class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        frq = {}
        for i in range(0,n+1):
            frq[i] = 0
        for num in nums:
            frq[num] = 1
        for k,v in frq.items():
            if v == 0:
                return k
        