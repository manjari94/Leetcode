class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        str_splt = list(s)
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if len(stack)!=0:
                    stack.pop()
                else:
                    str_splt[i]=""
        for i in stack:
            str_splt[i]=""
        return ''.join(str_splt)
