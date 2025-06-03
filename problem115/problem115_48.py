

def resolve():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip())

    print(n + n*n + n*n*n)

if __name__ == "__main__":
    resolve()
