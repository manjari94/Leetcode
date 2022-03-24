######### Longest Common Substring ###########
def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs)==0:
            return prefix
        elif len(strs)==1:
            return strs[0]
        else:
            new = strs.sort()
            for i in strs[0]:
                if strs[-1].startswith(prefix+i):
                    prefix += i
                else:
                    break
            return prefix
