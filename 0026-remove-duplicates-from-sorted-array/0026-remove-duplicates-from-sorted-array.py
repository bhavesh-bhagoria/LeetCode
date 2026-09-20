class Solution:
    def removeDuplicates(self, nums):
   
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
                
            else:
                i+=1
                j+=1
        
                
       