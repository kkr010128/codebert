def main():
    N = [int(x) for x in input()]
    dp0 = 0
    dp1 = 1
    for n in N:
        # そのまま払う
        a = min(dp0 + n, dp1 + 10 - n)
        # 1多めに払う
        b = min(dp0 + n + 1, dp1 + 10 - (n+1))
        dp0, dp1 = a, b
        
    print(dp0)
 
 
if __name__ == '__main__':
    main()