n = int(input())
A = list(map(int, input().split()))
q = int(input())
S = []
for _ in range(q):
    x, y = map(int, input().split())
    S.append((x, y))

sum = sum(A)
# print(sum)
R = [0 for _ in range(10**5+1)]
for a in A:
    R[a-1] += 1

for (x,y) in S:
    sum += (y-x)*R[x-1]
    R[y-1] += R[x-1]
    R[x-1] = 0
    print(sum)