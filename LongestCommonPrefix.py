class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        i=0
        if size==0:
            return 0
        if size==1:
            return strs[0]
        strs.sort()
        lcd = min(len(strs[0]),len(strs[size-1]))
        while(i<lcd and strs[0][i]==strs[size-1][i]):
            i=i+1
        prefix = strs[0][0:i]
        return prefix
        