class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force unoptimized
#         output = []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     output = [i,j]
#                     return output
#         return -1
        #hashmap optimized approach
        # hashmap = {}
        # result = []
        # for i in range(len(nums)):
        #     idx = target-nums[i]
        #     if idx in hashmap:
        #         result = [i,hashmap[idx]]
        #     else:
        #         hashmap[nums[i]]=i
        # return result
        #two pointer approach
        nums.sort()
        pointer1 = 0
        pointer2 = len(nums)-1
        while pointer1<pointer2:
            if nums[pointer1]+nums[pointer2]==target:
                return [pointer1,pointer2]
            elif nums[pointer1]+nums[pointer2]<target:
                pointer1 += 1
            elif nums[pointer1]+nums[pointer2]>target:
                pointer2 -= 1
            
