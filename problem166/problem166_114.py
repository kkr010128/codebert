import sys
sys.setrecursionlimit(10**9)

def main():
    S = [int(s) for s in input()]
    N = len(S)
    K = 2019

    V = [0] * (N+1)
    for i in reversed(range(N)):
        rev_i = (N-1)-i
        V[rev_i+1] = V[rev_i] + S[i] * (pow(10,rev_i+1,K))
        # print(V)

    dic = {} # value:count
    U = set()
    for v in V:
        u = v % K
        if u in U:
            dic[u] += 1
        else:
            dic[u] = 1
            U.add(u)

    ans = 0
    for u in U:
        u_count = dic[u]
        ans += u_count * (u_count-1) // 2

    # print(S)
    # print(V)
    # print(dic)
    print(ans)

if __name__ == "__main__":
  main()