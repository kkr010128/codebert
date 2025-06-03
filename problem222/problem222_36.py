n = int(input())
a = list(map(int,input().split()))
x = set(a)


print("YES" if len(x) == len(a) else "NO")