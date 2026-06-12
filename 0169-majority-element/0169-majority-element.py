class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        count = 1
        n= len(nums)
        for i in range(n):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = count
            elif nums[i] in hash_map:
                hash_map[nums[i]] +=1
        return max(hash_map, key=hash_map.get)