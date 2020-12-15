#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        out_l = ListNode()
        temp1,temp2,tempn = l1,l2,out_l
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                tempn.next = temp1
                temp1 = temp1.next
            else:
                tempn.next = temp2
                temp2 = temp2.next
            tempn = tempn.next
            
        tempn.next = temp1 if temp1 else temp2
        return out_l.next

