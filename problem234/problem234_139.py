from collections import deque

N = input()
digit = len(N)
f_digit = int(N[0])
l_digit = int(N[-1])
N = int(N)
cnt = 0

g_cnt = [[0]*10 for _ in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        g_cnt[i][j] = 0
        if i == j:
            if i <= N:
                g_cnt[i][j] += 1
            if i*10+i <= N:
                g_cnt[i][j] += 1
        else:
            if i*10+j <= N:
                g_cnt[i][j] += 1

        if digit >= 3:
            num = deque([str(k) for k in range(10)])
            while num:
                q = num.popleft()
                for k in range(10):
                    if int(str(i)+q+str(k)+str(j)) <= N:
                        num.append(q+str(k))
                if int(str(i)+q+str(j)) <= N:
                    g_cnt[i][j] += 1

for i in range(1, 10):
    for j in range(i, 10):
        if i == j:
            cnt += g_cnt[i][j] ** 2
        else:
            cnt += g_cnt[i][j] * g_cnt[j][i] * 2

print(cnt)