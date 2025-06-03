import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solve():
    def min2(x, y): return x if x <= y else y

    N = int(input())
    As = list(map(int, input().split()))

    if N == 0:
        if As[0] == 1:
            return 1
        else:
            return -1

    pow2 = 1
    pow2s = [pow2]
    for d in range(61):
        pow2 *= 2
        pow2s.append(pow2)
    pow2s += [pow2] * N
#    print('pow2s:', pow2s)

    maxV = min2(1, 1-As[0])
    maxVs = [maxV]
    for d in range(1, N+1):
        maxV = min2(maxV*2, pow2s[d]) - As[d]
        maxVs.append(maxV)
#    print('maxVs:', maxVs)

    numVs = [0] * (N+1)
    numVs[N] = As[N]
    for d in reversed(range(N)):
#        print('\n##### d:', d)
        numC2 = -(-numVs[d+1] // 2)
#        print('numC2:', numC2)
        if maxVs[d] < numC2:
            return -1
        num = min2(maxVs[d], numVs[d+1])
        numVs[d] = As[d] + num
#        print('As[d]:', As[d], '/ num:', num, '/ numVs[d]:', numVs[d])
        if numVs[d] > pow2s[d]:
            return -1

#    print('numVs:', numVs)
    return sum(numVs)


ans = solve()
print(ans)
