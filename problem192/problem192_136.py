def solve():
    import collections
    N = int(input())
    A = [int(i) for i in input().split()]
    counter = collections.Counter(A)
    combis = {}
    total = 0
    for k,v in counter.items():
        combi = v * (v-1) // 2
        combis[k] = combi
        total += combi
    for i in range(N):
        cnt = counter[A[i]]
        if cnt > 1:
            combi = (cnt-1) * (cnt-2) // 2
        else:
            combi = 0
        print(total - combis[A[i]] + combi)

if __name__ == "__main__":
    solve()