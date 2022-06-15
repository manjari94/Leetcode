class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ocean_view = []
        n = len(heights)
        maxR=0
        #right most building will always have ocean view
        ocean_view = [n-1]
        for i in range(n-2,-1,-1):
            maxR = max(maxR,heights[i+1])
            if maxR<heights[i]:
                ocean_view.append(i)
        return ocean_view[::-1]
