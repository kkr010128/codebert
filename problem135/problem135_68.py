def solve():
    A,B = input().split()
    A = int(A)
    B = int(''.join(B.split('.')))
    print(A*B//100)

if __name__ == "__main__":
    solve()