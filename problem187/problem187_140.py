import numpy as np
N, X, Y = [int(_) for _ in input().split()]
X -= 1
Y -= 1
cnt = np.zeros(N, dtype=int)
for i in range(0, (X + Y) // 2):
    #t-i<=abs(i-X)+1+Y-t
    #2*t<=abs(i-X)+1+Y+i
    #t<= tmax = 0 - - (abs(i-X)+1+Y+i)//2
    #tmin=abs(i-X)+1
    tmin = abs(i - X) + 1
    tmax = 0 - -(abs(i - X) + 1 + Y + i) // 2
    cnt[1:tmax - i] += 1
    cnt[tmin:tmin + Y - tmax + 1] += 1
    cnt[tmin + 1:tmin + N - Y] += 1
for i in range((X + Y) // 2, N):
    cnt[1:N - i] += 1
print(*cnt[1:], sep='\n')
