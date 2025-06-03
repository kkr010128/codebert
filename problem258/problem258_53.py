def resolve():
    N = int(input())
    if N%2 == 1:
        print(0)
    else:
        ans = 0
        for i in range(0, 50):
            ans += N//(10*(5**i))
        print(ans)
    
if __name__ == "__main__":
    resolve()

