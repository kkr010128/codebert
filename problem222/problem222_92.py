n = int(input())
a = [int(s) for s in input().split()]
if len(set(a)) == n:
    print("YES")
else:
    print("NO")