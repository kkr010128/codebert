N = int(input())
A = list(map(int, input().split()))
d = []
for n in range(N):
    d.append([A[n], n])
d = sorted(d, key=lambda x:x[0])
for i, j in d:
    print(j+1, end=" ")