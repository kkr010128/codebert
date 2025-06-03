import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N,*ab = map(int, read().split())

    A, B = [], []
    for a, b in zip(*[iter(ab)]*2):
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()

    if N % 2 == 0:
        a1, a2 = A[N // 2 - 1], A[N // 2]
        b1, b2 = B[N // 2 - 1], B[N // 2]

        ans = b1 + b2 - (a1 + a2) + 1
    
    else:
        a = A[N // 2]
        b = B[N // 2]
        
        ans = b - a + 1
    
    print(ans)


if __name__ == "__main__":
    main()
