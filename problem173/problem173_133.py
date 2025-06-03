def solve(n):
    arr = [i for i in range(1, n+1) if i % 3 != 0 and i % 5 != 0]
    print(sum(arr))

if __name__ == "__main__":
    n = int(input())
    solve(n)