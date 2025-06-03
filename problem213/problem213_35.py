def mapt(fn, *args):
    return tuple(map(fn, *args))

def main():
    n = int(input())
    x = mapt(int, input().split(" "))
    ans = float("inf")
    for p in range(1, 101):
        r = 0
        for xj in x:
            r += (xj-(p))**2
        ans = min(ans, r)
    print(ans)

main()