N = int(input())
A = list(map(int,input().split()))
bunretsu = sum(A) - 1
zanretsu = 1
souwa = 0
for i in range(N+1):
    souwa += zanretsu
    if A[i] <= zanretsu:
        zanretsu -= A[i]
    else:
        souwa = -1
        break
    if bunretsu >= 1 and bunretsu <= zanretsu:
        zanretsu += bunretsu
        bunretsu = 0
    elif bunretsu >= 1 and bunretsu > zanretsu:
        bunretsu -= zanretsu
        zanretsu *= 2
print(souwa)