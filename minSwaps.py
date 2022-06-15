class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        swap = 0
        for i in s:
            if i=='[':
                count += 1
            else:
                count -= 1
                if count<0:
                    swap += 1
                    count=0
        return swap
