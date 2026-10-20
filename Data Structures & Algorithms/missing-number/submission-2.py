class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_max = len(nums)

        arr = list(range(n_max+1))

        for i in arr:
            if i not in nums:
                return int(i)
           
            

        