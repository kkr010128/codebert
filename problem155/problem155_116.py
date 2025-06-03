def main():

    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    connected = dict()
    for _ in range(M):
        A, B = map(int, input().split())
        if A not in connected:
            connected[A] = H[B-1]
        else:
            connected[A] = max(connected[A], H[B-1])
        if B not in connected:
            connected[B] = H[A-1]
        else:
            connected[B] = max(connected[B], H[A-1])

    ans = 0
    for i in range(1, N+1):
        if i not in connected:
            ans += 1
        elif H[i-1] > connected[i]:
            ans += 1
    return ans

if __name__ == '__main__':
    print(main())
