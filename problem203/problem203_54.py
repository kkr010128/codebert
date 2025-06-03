import math

def solve():
    A, B = [int(i) for i in input().split()]
    a = A / 0.08
    b = B / 0.1
    mi = min(a, b)
    ma = max(a, b)
    for i in range(math.floor(mi), math.ceil(ma) + 1):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            exit()
    print(-1)

if __name__ == "__main__":
    solve()