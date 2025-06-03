def solve():
    N = int(input())
    items = set([])
    for i in range(N):
        S = input()
        items.add(S)
    print(len(items))

if __name__ == "__main__":
    solve()