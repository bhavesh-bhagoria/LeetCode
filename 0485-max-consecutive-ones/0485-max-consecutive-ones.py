class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for v in nums:
            if v == 1:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 0
        if curr:
            ans = max(ans, curr)
        return ans