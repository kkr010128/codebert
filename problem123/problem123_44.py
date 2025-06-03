n = int(input())
a = [int(i) for i in input().split(" ")]
t = a[0]
for i in a[1:]:
    t = t ^ i
ans = [t^i for i in a]
print(" ".join(map(str, ans)))