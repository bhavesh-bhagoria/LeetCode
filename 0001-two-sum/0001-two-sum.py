class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len (nums)
        target_list =[]
        if n<=2:
            target_list.append(0)
            target_list.append(1)
            return target_list
        

        for i in range(n):
            for j in range(i,n):
                if nums[i]+nums[j] == target and i!=j:
                    target_list.append(i)
                    target_list.append(j)
        return target_list