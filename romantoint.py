######## ROMAN TO INTEGER ##########

 def romanToInt(self, s: str) -> int:
        sym = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        for i in range(0,len(s)-1):
            if sym[s[i]]<sym[s[i+1]]:
                sum = sum - sym[s[i]]
            else:
                sum = sum + sym[s[i]]
        return sum+sym[s[-1]]
