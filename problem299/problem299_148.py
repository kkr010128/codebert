N = int(input())
A = list(map(int, input().split()))

dic = {i:0 for i in range(1, N + 1)}


for i in range(N):
    a = A[i]
    dic[a] = i + 1

for i in range(1, N + 1):
    print(dic[i], end="")
    if i != N:
        print(" ", end="")

print()