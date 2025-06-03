from functools import lru_cache


@lru_cache(maxsize=None)
def get_dividers(n):
    """
    正の整数 n の約数を取得する
    """

    dividers = {i for i in range(1, int(n ** 0.5) + 1) if n % i == 0}
    return dividers | {n // d for d in dividers}


A, B = map(int, input().split(' '))

a_dividers = get_dividers(A)
b_dividers = get_dividers(B)
common_dividers = a_dividers & b_dividers
ans = []

for cd in sorted(common_dividers):
    dividers = get_dividers(cd) - {1}
    for d in ans:
        if d & dividers:
            break
    else:
        ans.append(dividers)

print(len(ans))
