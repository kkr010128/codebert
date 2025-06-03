N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
ruiseki_A = [0]
ruiseki_B = [0]
 
for i in range(len(A)):
    ruiseki_A.append(ruiseki_A[i]+A[i])
for i in range(len(B)):
    ruiseki_B.append(ruiseki_B[i]+B[i])
#print(ruiseki_A)
 
ans = 0
for i in range(len(ruiseki_A)):
    tmp = K - ruiseki_A[i]
    if tmp < 0:
        continue
    r = len(ruiseki_B)
    l = 0
    while r-l > 1:
        mid = (r + l) // 2
        if ruiseki_B[mid] <= tmp:
            l = mid
        else:
            r = mid
    ans = max(ans, i+l)
 
print(ans)