H = int(input())
W = int(input())
N = int(input())
cnt=wcnt=hcnt=0

while N>0:
    a = max(H-hcnt, W-wcnt)
    N -= a
    cnt+=1
    if a==W:
        H-=1
        hcnt+=1
    elif a==H:
        W-=1
        wcnt+=1
print(cnt)