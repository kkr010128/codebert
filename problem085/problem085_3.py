N = int(input())
A = [int(x) for x in input().split()]

# M以下の整数の素因数分解を高速に
# 前処理O(MloglogM)
# 一計算O(logK)
def mae_syori(M):
    D = [0] * (M + 1)
    for i in range(2, M+1):
        if D[i] != 0: continue
    #     print(i, list(range(i*2, M + 1, i)))
        for j in range(i*2, M+1, i):
            if D[j] == 0:
                D[j] = i
    return D

def p_bunkai(K):
    assert 2 <= K <= len(D)-1
    k = K
    ret = []
    while True:
        if k == 1:
            break
        if D[k] == 0:
            ret.append((k, 1))
            break
        else:
            p = D[k]
            count = 0
            while k % p == 0:
                count += 1
                k //= p
            ret.append((p, count))
    return ret
 

# 最大公約数
# ユークリッドの互除法
def my_gcd(a, b):
    if b == 0:
        return a
    else:
        return my_gcd(b, a%b)

c_gcd = A[0]
for a in A:
    c_gcd = my_gcd(c_gcd, a)

if c_gcd == 1:
    max_A = max(A)
    D = mae_syori(max_A)
    yakusu = set()
    ok = True
    for a in A:
        if a == 1: continue
        p_bunkai_result = p_bunkai(a)
        p_list = [p[0] for p in p_bunkai_result]
        for p in p_list:
            if p not in yakusu:
                yakusu.add(p)
            else:
                ok = False
        if not ok:
            break
    if ok:
        print('pairwise coprime')
    else:
        print('setwise coprime')
else:
    print('not coprime')