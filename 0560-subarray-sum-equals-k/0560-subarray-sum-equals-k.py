class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        ans = 0
        hash_map = {0: 1}

        for x in nums:
            total += x

            if total - k in hash_map:
                ans += hash_map[total - k]

            if total in hash_map:
                hash_map[total] += 1
            else:
                hash_map[total] = 1

        return ans