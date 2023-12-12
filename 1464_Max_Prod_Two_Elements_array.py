class Solution:
    def maxProduct(self, nums):
        n  = len(nums)
        max_prod = 0
        for i in range(0,n):
            for j in range(1, n):
                if i != j:
                    prod = (nums[i] - 1) * (nums[j] - 1)
                    max_prod = max((max_prod, prod))
                    
        return max_prod