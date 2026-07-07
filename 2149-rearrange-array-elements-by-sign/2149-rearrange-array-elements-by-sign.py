class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive = []
        negative = []
        for x in range(n):
            if nums[x]>0:
                positive.append(nums[x])
            else:
                negative.append(nums[x])
        i = 0
        j = 0
        k = 0
        while i < len(positive) and j < len(negative):
            nums[k] = positive[i]
            nums[k + 1] = negative[j]
            i+=1
            j+=1
            k+=2
        return nums
