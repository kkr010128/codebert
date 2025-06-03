
def solve():
    ans = 10**12
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans = min(ans, i + (N//i) -2)
    if N == 2:
        print(1)
    elif N == 3:
        print(2)
    else:
        print(ans)
            
if __name__ == "__main__":  
    N = int(input())
    solve()  
