H=int(input())
W=int(input())
N=int(input())
B=max(H,W)
ans=(N+B-1)//B
print(ans)