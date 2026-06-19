class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n= len(nums)
        hash_map={}
        count = 0
        for i in range(n):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                del hash_map[nums[i]]
        for ans in hash_map:
            return ans
       
                