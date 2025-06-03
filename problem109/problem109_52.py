n=int(input())
l=['AC','WA','TLE','RE']
d=[0,0,0,0]
for i in range(n):
    s=input()
    if(s=='AC'):
        d[0]+=1
    elif(s=='WA'):
        d[1]+=1
    elif(s=='TLE'):
        d[2]+=1
    else:
        d[3]+=1
for i in range(4):
    print(l[i],'x',d[i])
