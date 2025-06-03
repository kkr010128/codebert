n=int(input())
score=[0,0,0]
for _ in range(n):
    tc,hc=map(str,input().split())
    if tc==hc:
        score[1]+=1
        score[-1]+=1
        continue
    i=0
    ml=min(len(tc),len(hc)) 
    while tc[i]==hc[i]:
        i+=1
        if i>=ml:
            tc+="0"
            hc+="0"
            break
    r=ord(tc[i])-ord(hc[i])
    r=r//abs(r)
    score[r]+=3

print("{} {}".format(score[1],score[-1]))
