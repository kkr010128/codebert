# ABC154A

def f(s, t, a, b, u):
    if u == s:
        print(a - 1, b)
    else:
        print(a, b - 1)

s, t = input().split()
a, b = map(int, input().split())
u = input()

f(s, t, a, b, u)
