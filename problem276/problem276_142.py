import math

def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    S = sum(A)
    l = A[0]
    I = 0
    m = math.ceil(S / 2)
    for i in range(1, N):
        if (l + A[i]) <= m:
            l += A[i]
        else:
            I = i - 1
            break
    if l == S / 2:
        print(0)
        exit()
    c = A[I + 1]
    r = S - l - c
    ans1 = abs(r - (l + c))
    ans2 = abs(l - (r + c))
    print(min(ans1, ans2))

if __name__ == "__main__":
    solve()
