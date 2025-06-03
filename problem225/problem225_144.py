def solve():
    H,A = [int(i) for i in input().split()]
    print((H+A-1)//A)
    
if __name__ == "__main__":
    solve()