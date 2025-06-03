N, K = map(int, input().split())
H = map(int, input().split())
if K >= N:
    print(0)
    exit()

H = list(H)
H.sort()
print(sum(x for x in H[0 : N - K]))