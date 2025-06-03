H=int(input())
W=int(input())
N=int(input())
k=max(H, W)
cnt=0
while k*cnt<N:
    cnt+=1
print(cnt)