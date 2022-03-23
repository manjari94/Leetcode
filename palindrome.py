###LEETCODE EASY####

def isPalindrome(self, x: int) -> bool:
        temp = list(str(x))
        if temp == temp[::-1]:
            return True
        else:
            return False
