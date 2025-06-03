N = int(input())
h = int(N / 2)
a = input().split()
for i in range(h):
    t = a[i]
    a[i] = a[N-1-i]
    a[N-1-i] = t
print(" ".join(a))   