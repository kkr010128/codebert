import collections

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    H, W, K = ZZ()
    C = [input() for _ in range(H)]
    atode = collections.deque()
    last = -1
    cakeId = 0
    output = [[0] * W for _ in range(H)]

    for i in range(H):
        if not '#' in C[i]:
            atode.append(i)
            continue
        ichigo = []
        last = i
        for j in range(W):
            if C[i][j] == '#': ichigo.append(j)
        itr = 0
        for j in ichigo:
            cakeId += 1
            while itr <= j:
                output[i][itr] = cakeId
                itr += 1
        while itr < W:
            output[i][itr] = cakeId
            itr += 1
        while atode:
            j = atode.popleft()
            for k in range(W): output[j][k] = output[i][k]
    while atode:
        j = atode.popleft()
        for k in range(W): output[j][k] = output[last][k]

    for i in range(H): print(*output[i])

    return

if __name__ == '__main__':
    main()
