n,k = map(int,input().split())
li = list(map(int,input().split()))
licsum = [0]
for i in range(n):
    licsum.append(licsum[i] + li[i])
lia = []
for i in range(n-k+1):
    a = licsum[k+i] - licsum[i] + k
    lia.append(float(a)/2)
print(max(lia))