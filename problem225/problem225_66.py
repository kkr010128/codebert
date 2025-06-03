# ABC153A

def f(h, a):
    ans = h // a
    if ans * a < h:
        ans += 1
    print(ans)

h, a = map(int, input().split())
f(h, a)
