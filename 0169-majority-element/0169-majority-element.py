class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        count = 1
        n= len(nums)
        for f in range(n):
            if nums[f] not in hash_map:
                hash_map[nums[f]] = count
            elif nums[f] in hash_map:
                hash_map[nums[f]] +=1
        return max(hash_map, key=hash_map.get)