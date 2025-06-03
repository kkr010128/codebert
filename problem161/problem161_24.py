import math
A, B, N = map(int, input().split())
ans = []
if B-1<N:
    sahen = math.floor(A*(B-1)//B)
    uhen = math.floor((B-1)//B)
    uhen = uhen*A
    ans.append(sahen-uhen)

sahen = math.floor(A*N//B)
uhen = math.floor(N//B)
uhen = uhen*A
ans.append(sahen-uhen)

print(max(ans))
