if len(colors)<3:
            return False
        alice, bob = 0, 0
        i = 0
        while i<len(colors)-2:
            if colors[i]==colors[i+1] and colors[i]==colors[i+2]: #minimum consecutive length of 3 with same characters for player to remove
                if colors[i]=='A':
                    alice += 1
                else:
                    bob += 1
            i=i+1
        return alice>bob #if bob could not make the last move then alice>bob will be true meaning Alice won and if bob made the last move the alice>bob returns false which means Bob won
