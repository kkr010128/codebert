N = int(input())
A = list(map(int, input().split()))

b = [0] * N
for a in A:
    b[a-1] += 1
for i in b:
    print(i)