N,M = map(int,input().split())
S = input()

ans = []
right = N

while right > 0:
    left = right
    for i in range(M):
        if S[right-i-1] == '0':
            left = right-i-1
        if left == 0:
            break
    if left == right:
        print(-1)
        break
    ans.append(right-left)
    right = left
else:
    print(*reversed(ans))