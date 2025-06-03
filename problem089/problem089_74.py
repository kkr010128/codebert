H, W, m = map(int, input().split())

H_bomb = [0]*H
W_bomb = [0]*W
S = set()

for _ in range(m):
    h, w = map(int, input().split())
    h, w = h-1, w-1
    S.add(tuple([h, w]))
    H_bomb[h] += 1
    W_bomb[w] += 1

H_max = max(H_bomb)
W_max = max(W_bomb)

H_memo = set()
W_memo = set()

for i in range(H):
    if H_bomb[i] == H_max:
        H_memo.add(i)

for j in range(W):
    if W_bomb[j] == W_max:
        W_memo.add(j)

ans = H_max + W_max

# for i in H_memo:
#     for j in W_memo:
#         if tuple([i, j]) not in S:
#             print(ans)
#             exit()

cnt = 0
for s in S:
    if s[0] in H_memo and s[1] in W_memo:
        cnt += 1

if cnt == len(H_memo)*len(W_memo):
    print(ans-1)
else:
    print(ans)