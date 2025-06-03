H = int(input())
W = int(input())
N = int(input())

big = max(H,W)
bigsum = 0
ans = 0

while bigsum < N:
    bigsum += big
    ans += 1
    
print(ans)
