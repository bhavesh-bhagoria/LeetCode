class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        x=0
        y=n
        while x<k:
            y=n
            item = nums.pop(y-1)
            nums.insert(0,item)
            x+=1
            y+=1

           

