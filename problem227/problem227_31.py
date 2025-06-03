N,K=list(map(int, input().split()))
H=list(map(int, input().split()))

if K>=N:
    print(0)
    exit()
H.sort(reverse=True)
H=H[K:]
print(sum(H))