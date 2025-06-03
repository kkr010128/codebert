N = int(input())
L = list(map(int, input().split()))
L.sort()

cnt = 0
for i in range(N-2):
    for j in range(i, N-1):
        for k in range(j, N):
            a, b, c = L[i], L[j], L[k]
            if a == b or b == c or c == a:
                continue
            elif a+b>c and b+c>a and c+a>b:
                cnt+=1

print(cnt)
