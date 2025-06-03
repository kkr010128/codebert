n = int(input())

a = list(map(int, input().split()))
b = list(enumerate(a))
c = sorted(b, key=lambda x:x[1])


print(*[c[i][0]+1 for i in range(n)])