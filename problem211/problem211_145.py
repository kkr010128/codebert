def solve():
    N,R = [int(i) for i in input().split()]
    if N >= 10:
        print(R)
    else:
        print(R+100*(10-N))

if __name__ == "__main__":
    solve()