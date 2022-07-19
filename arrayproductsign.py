class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        count = len(list(filter(lambda x : (x<0), nums)))
        if count%2==0:
            return 1
        else:
            return -1
