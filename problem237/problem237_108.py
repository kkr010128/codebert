# お尻から見ていってはやく終わるを数え上げれば良い
N = int(input())
data = []
for _ in range(N):
    X, L = map(int, input().split())
    data.append((X-L, X+L))
data = sorted(data, key=lambda x: x[1])
count = 1
j = 0
for i in range(1, N):
    if data[i][0] >= data[j][1]:
        j = i
        count += 1
print(count)
