def solve():
    S,T = input().split()
    A,B = [int(i) for i in input().split()]
    U = input()

    if U == S:
        print(A-1, B)
    else:
        print(A, B-1)

if __name__ == "__main__":
    solve()