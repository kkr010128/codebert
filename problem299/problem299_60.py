n = int(input())
a = list(map(int, input().split()))
alist = [0]*n

for i in range(n):
    alist[a[i]-1] = str(i+1)

print(" ".join(alist))