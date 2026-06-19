class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        ans = -1
        window = 0
        n = len(nums)
        for right in range(n):
            window+= nums[right]
            while(right-left+1!=window):
                window-=nums[left]
                left+=1
            ans=max(ans,right-left+1)
        return ans