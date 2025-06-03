def solve():
    a,b = [int(i) for i in input().split()]
    smaller = min(a, b)
    bigger = max(a, b)
    print(''.join([str(smaller)]*bigger))

if __name__ == "__main__":
    solve()