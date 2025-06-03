N, K = map(int, input().split(' '))
h_ls = map(int, input().split(' '))
cnt = 0
for i in h_ls:
    if i >= K:
        cnt += 1
print(cnt)