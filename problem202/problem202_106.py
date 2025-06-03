
def main():
    n, a, b = map(int, input().split(" "))
    one_round = a+b
    x = n // one_round
    n = n % one_round
    ans = x * a
    ans += min(n,a)
    print(ans)
if __name__ == "__main__":
    main()