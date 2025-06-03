n = int(input().split()[0])
c = list(map(int,input().split()))
minimum = [ i for i in range(n+1) ]

for i in range(2,n+1):
    for j in c:
        if j <= i and minimum[i-j] + 1 < minimum[i]:
            minimum[i] = minimum[i-j]+1

print(minimum[n])