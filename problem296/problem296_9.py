from itertools import groupby

# RUN LENGTH ENCODING str -> tuple
def run_length_encode(S: str):
    """
    'AAAABBBCCDAABBB' -> [('A', 4), ('B', 3), ('C', 2), ('D', 1), ('A', 2), ('B', 3)]
    """
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, len(list(v))))
    return res


S = input()
K = int(input())

if len(set(list(S))) == 1:
    print((len(S) * K) // 2)
else:
    rle = run_length_encode(S)
    cnt = 0
    for w, length in rle:
        if length > 1:
            cnt += length // 2

    ans = cnt * K
    if S[0] == S[-1]:
        a = rle[0][1]
        b = rle[-1][1]
        ans -= (a // 2 + b // 2 - (a + b) // 2) * (K - 1)
    print(ans)


