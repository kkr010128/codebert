n = int(input())
a = [int(i) for i in input().split()]
new_a = set(a)
if len(new_a) != n:
    print("NO")
else:
    print("YES")