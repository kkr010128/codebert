def solve():
    N = int(input())
    A = [int(i) for i in input().split()]

    set_A = set([])
    for num in A:
        if num in set_A:
            print('NO')
            return
        set_A.add(num)
    print('YES')

if __name__ == "__main__":
    solve()