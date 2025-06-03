# def gen_is_prim(n):
#     is_prim = [i%2==1 for i in range(n+1)]
#     is_prim[1] = False; is_prim[2] = True
#     for i in range(3, n+1, 2):
#         if not is_prim[i]: continue
#         for j in range(i+i, n+1, i):
#             is_prim[j] = False
#     return is_prim

def gen_d_prim(n):
    D = [n+1 if i%2 else 2 for i in range(n+1)]
    D[0] = D[1] = 0
    for i in range(3, n+1, 2):
        if D[i] != n+1: continue
        for j in range(i, n+1, i): D[j] = i
    return D

def gcd_all(A):
    from math import gcd
    g = 0
    for a in A: g = gcd(g, a)
    return g

def is_pairwise():
    # MAX_A = 10**6 + 1
    # C = [0] * MAX_A
    # for a in A: C[a] += 1
    # if sum(C[2::2]) > 1: return False
    # for i in range(3, MAX_A, 2):
    #     if sum(C[i::i]) > 1: return False
    # return True

    MAX_A = 10**6
    D = gen_d_prim(MAX_A)
    C = [0] * (MAX_A + 1)
    all_p = set()
    for a in A:
        p = set()
        while a != 1:
            if not D[a] in p:
                if D[a] in all_p:
                    return False
            all_p.add(D[a])
            p.add(D[a])
            a //= D[a]
        # print('pre {}'.format(pre))
        # print('now {}'.format(now))
        # print('now & pre {}'.format(now & pre))
        # if len(now & all) > 0: return False
        # all = all | now
    return True

def solve():
    if is_pairwise(): return 0
    if gcd_all(A) == 1: return 1
    return 2

    # if gcd_all(A) > 1: return 2
    # if is_pairwise(): return 0
    # return 1


n = int(input())
A = [*map(int, input().split())]
print(['pairwise','setwise','not'][solve()], 'coprime')
