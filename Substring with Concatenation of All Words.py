   res = []
    WordLen = [len(s) for s in words]
    WordIni = [  s[0] for s in words]
    TotWordLen =     sum(WordLen)
    LongestWordLen = max(WordLen)
    
    d = {}
    for i in range(len(words)):
        if words[i] not in d:
            d[words[i]] = [i]
        else:
            d[words[i]].append(i) 
            
    
    def isCCT(string):
        
        copy_d = copy.deepcopy(d)
        temp = ''
        #print('isCCT:',string,copy_d)
        
        for c in string:
            temp += c
            if temp in copy_d:
                
                if len(copy_d[temp]) > 1:
                    copy_d[temp].pop()
                else:
                    del copy_d[temp]
                temp = ''
            elif len(temp) >= LongestWordLen:
                #print('isCCT:',string, temp, 'zero patience')
                return False
        
        #print('isCCT:',string, temp)    
        if temp == '' and len(copy_d) == 0:
            return True
        else:
            return False
    
    
    for i in range(len(s)):
        if s[i] in WordIni:
            if (i + TotWordLen - 1) <= len(s): 
                testSubStr = s[i:i + TotWordLen]
                #print(i,testSubStr)
                if isCCT(testSubStr) == True:
                    res.append(i)
                
    return res
```**Please Don't forget to UPVOTE if you LIKE!!**
