class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force unoptimized
        # Time complexity : O(n^2)
        output = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    output = [i,j]
                    return output
        return -1
            
