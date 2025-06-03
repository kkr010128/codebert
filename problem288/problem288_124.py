import math
N = int(input())
ans = N - 1 #初期値、√Nの中に答えがなかったときはこれ
t = int(math.ceil(N**0.5))

for i in range(1,t+1):
    j = N / i
    if N % i == 0:
        step = i + j -2
        if step < ans:
            ans = int(step)
print(ans)