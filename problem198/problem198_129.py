
n = int(input())

stack = [["",0] for i in range(10**6*4)]
stack[0] = ["a",1]
pos = 0    
while(pos>=0):
    if(len(stack[pos][0]) == n):
        print(stack[pos][0])
        pos-=1
    else:
        
        nowstr = stack[pos][0]
        nowlen = stack[pos][1]
        #print(nowlen)
        pos-=1
        for ii in range(nowlen+1):
            i = nowlen-ii
            pos+=1
            stack[pos][0] = nowstr+chr(ord('a')+i)
            if(i == nowlen):
                stack[pos][1] = nowlen+1
            else:
                stack[pos][1] = nowlen



