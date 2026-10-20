class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       

        for i in list(range(len(nums)+1)):
            if i not in nums:
                return int(i)
           
            

        