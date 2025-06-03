N = int(input())
c = input()
len_r = 0
len_w = 0
for i in range(N):
    if c[i] == 'R':
        len_r += 1
len_w = N - len_r
n_r = 0
for j in range(len_r):
    if c[j] == 'R':
        n_r += 1
ans = len_r - n_r
print(ans)