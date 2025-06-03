import copy

def bit_list(x: int, n: int) -> list:
    '''
    xのn乗のbit配列を返す
    '''
    ans = []
    for i in range(x ** n):
        num = i
        j = 0
        table = [0 for _ in range(n)]
        while num:
            table[j] = num % x
            num = num // x
            j += 1

        ans.append(table)

    return ans

H, W, K = map(int, input().split())
M = [list(input()) for _ in range(H)]

ans = 0
bits = bit_list(2, H + W)

for bit in bits:
    tmp_M = copy.deepcopy(M)
    for i in range(H + W):
        if i < H and bit[i] == 1:
            for j in range(W):
                 tmp_M[i][j] = "R"
        if i >= H and bit[i] == 1:
            for j in range(H):
                 tmp_M[j][i - H] = "R"

    count = 0
    for i in range(H):
        for j in range(W):
            if tmp_M[i][j] == '#':
                count += 1

    if count == K:
        ans += 1

print(ans)