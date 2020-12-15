#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev,curr=0,0
        for curr in range(1,len(nums)):
            if(nums[prev]!=nums[curr]):
                prev += 1
                nums[prev]=nums[curr]
        nums = nums[:prev+1]
        return(len(nums))
        return(nums)

