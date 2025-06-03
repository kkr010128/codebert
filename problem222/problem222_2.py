n = int(input())
a = list(map(int, input().split()))
b = set(a)
a.sort()
if len(a) != len(b):
    print("NO")
else:
    print("YES")