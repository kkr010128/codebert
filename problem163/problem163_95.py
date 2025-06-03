def resolve():
    S, W = list(map(int, input().split()))
    print("unsafe" if S <= W else "safe")

if '__main__' == __name__:
    resolve()