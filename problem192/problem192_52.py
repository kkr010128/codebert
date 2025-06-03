def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    import collections
    counter = collections.Counter(A)
    total = 0
    for k, v in counter.items():
        total += v*(v-1)//2
    
    for a in A:
        cnt = counter[a]
        cntm1 = cnt - 1
        print(total - cnt*(cnt-1)//2 + cntm1*(cntm1-1)//2)


if '__main__' == __name__:
    resolve()