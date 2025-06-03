N, M = map(int, input().split())
if M%2 != 0:
    center = M + 1
else:
    center = M
c = center//2
d = (center + 1 + 2*M + 1) // 2

i = 0
while i < c:
    print(c-i, c+1+i)
    i += 1
j = 0
while i < M:
    print(d-(j+1), d+(j+1))
    i += 1
    j += 1