#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque
from queue import LifoQueue
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        par_set = {")":"(","]":"[","}":"{"}
        for ch in s:
            if ch in par_set:
                top = stack.pop() if stack else '#'
                if par_set[ch]!=top:
                    return False
            else:
                stack.append(ch)
                
                
        return not stack
        

