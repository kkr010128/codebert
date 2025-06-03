N = int(input())
a = list(map(int, input().split()))

# XOR演算子　^
# aの要素全てのXORを計算、それをSとする
S = 0
for aa in a:
    S ^= aa

# i番目の番号はaiとSのXORで表される
ans = []
for ai in a:
    ans.append(S ^ ai)

print(*ans)