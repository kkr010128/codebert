H = int(input())
W = int(input())
N = int(input())

N += max(H-1,W-1)

ans = N//max(H,W)

print(ans)