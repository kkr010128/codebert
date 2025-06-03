s, t = input().split()
a, b = map(int, input().split())
u = input()
if u == s:
    print(a-1, end = ' ')
    print(b)
else:
    print(a, end = ' ')
    print(b-1)