N = int(input())
D = []

for i in range(N):
    s, t = input().split()
    D.append([s, int(t)])

m = input()
n = 0
for i in range(N):
    if m in D[i]:
        n = i
        break

print(sum([d[1] for d in D[n + 1:]]))


