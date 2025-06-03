n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

def f(a):
    ans = 1
    if 0 in a:
        return 0
    for i in a:
        ans *= i
        if ans > 1e+18:
            return -1
    return ans

print(f(a))