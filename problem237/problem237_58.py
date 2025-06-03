N = int(input())
R = sorted([list(map(int, input().split())) for i in range(N)])
T = []
for i in range(N):
    T.append([R[i][0] + R[i][1], R[i][0] - R[i][1]])
T.sort(reverse=True)
while len(T) - 1 > 0:
    t = T.pop()
    i = 1
    while len(T) and t[0] > T[-1][1]:
        N -= 1
        i += 1
        T.pop()
print(N)