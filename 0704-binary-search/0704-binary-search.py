class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_target(start,end):
            if start>end:
                return -1
            middle = (start+end)//2
            if nums[middle] == target:
                return middle
            if nums[middle]<target:
                return find_target(middle+1,end)
            if nums[middle] > target:
                return find_target(start,middle-1)
        return find_target(0,len(nums)-1)

                

