N,K,C = map(int,input().split())
S = input()

left, right = [], []
d = 0
while d < N and len(left) < K:
    if S[d] == 'o':
        left.append(d)
        d += C + 1
    else:
        d += 1
d = N - 1
while d >= 0 and len(right) < K:
    if S[d] == 'o':
        right.append(d)
        d -= C + 1
    else:
        d -= 1
right.sort()

ans = []
for i in range(K):
    if left[i] == right[i]:
        ans.append(left[i])

for c in ans:
    print(c+1)