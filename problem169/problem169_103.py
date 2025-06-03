n = int(input())
A = list(map(int, input().split()))
T = [0]*n

for a in A:
    T[a-1] += 1

for t in T:
    print(t)