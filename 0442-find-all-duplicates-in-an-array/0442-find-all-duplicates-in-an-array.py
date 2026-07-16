class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        ans = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            if freq[num] == 2:
                ans.append(num)

        return ans