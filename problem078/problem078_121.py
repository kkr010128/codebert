def main2():
    N = int(input())
    mod = 10**9 + 7
    ans = 10**N - 9**N - 9**N + 8**N
    print(ans % mod)
    
if __name__ == "__main__":
    main2()