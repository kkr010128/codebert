n = int(input())
a = [0] + list(map(int, input().split()))

l = ["0"] * n
for i in range(1, n+1):
    l[a[i]-1] = str(i)

print(" ".join(l))