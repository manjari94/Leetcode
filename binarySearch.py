class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0 
        high=len(nums)-1
        while low<=high:
            mid = int((low+high)/2)
            m = nums[mid]
            if m==target:
                return mid
            elif m<target:
                low = mid+1
            elif m>target:
                high = mid-1
        return -1
