N = int(input())
X = list(map(int,input().split()))
avg = sum(X)//N
sums_1 = 0
sums_2 = 0
for i in X:
    sums_1 += (avg - i)**2

for j in X:
    sums_2 += (avg+1 - j)**2


print(min(sums_1,sums_2))