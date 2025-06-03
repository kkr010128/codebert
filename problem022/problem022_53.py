N = int(input())
L = input().split()
n = int(input())
l = input().split()
dup = []
count = 0
for i in range(N):
    for j in range(n):
        if L[i] == l[j]:
            dup.append(L[i])
            break
dup = list(set(dup))
print(len(dup))
