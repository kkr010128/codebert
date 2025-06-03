def func(S):
    T = S[::-1]
    ans = sum(1 for s, t in zip (S, T) if s != t) // 2
    return ans


if __name__ == "__main__":
    S = input()
    print(func(S))
