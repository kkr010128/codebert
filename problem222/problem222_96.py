n=int(input())
a=[int(x) for x in input().split()]
if len(a) == len(set(a)):
    print("YES")
else:
    print("NO")