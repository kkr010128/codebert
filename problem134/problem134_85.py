N = int(input())
S = list(map(int, input().split()))

def f():
    if 0 in S:
        return 0
    elif 10 ** 18 in S:
        return -1
    else:
        ans = 1
        for s in S:
            ans *= s
            if ans > 10 ** 18:
                return -1
        return ans

print(f())