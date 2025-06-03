n=int(input())
a=[int(i) for i in input().split()]
s=a[0]
for i in a[1:]:
    s^=i
print(*[s^i for i in a])