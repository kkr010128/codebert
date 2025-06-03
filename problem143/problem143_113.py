def solve():
    K = int(input())
    S = input()
    if len(S) > K:
        print("{}...".format(S[:K]))
    else:
        print(S)

if __name__ == "__main__":
    solve()