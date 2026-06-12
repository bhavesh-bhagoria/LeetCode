class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        if not nums:
            return False
        for i in range(len(nums)):
            count = 0
            if nums[i] in hash_map:
                count+=1
            hash_map[nums[i]] = count
        if max(hash_map.values()) > 0:
            return True 
        else:
            return False