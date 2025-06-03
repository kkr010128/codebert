n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = map(int, input().split())

count = 0
for key in T:
    U = S + [key]
    i = 0
    while U[i] != key:
        i = i+1
    if i != n:
        count = count + 1
print(count)