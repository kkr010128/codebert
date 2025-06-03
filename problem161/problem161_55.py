def solve():
    A,B,N = [int(i) for i in input().split()]
    x = min(B-1,N)
    print(int(A*x/B)-A*int(x/B))

if __name__ == "__main__":
    solve()