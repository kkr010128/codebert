n = int(input())
a = list(map(int,input().split()))
q = int(input())
bc = [list(map(int,input().split())) for i in range(q)]
list = [0]*(10**5)
for i in range(n) :
    list[a[i]-1] += 1

wa = sum(a)

for i in range(q) :
    wa += (bc[i][1]-bc[i][0])*list[bc[i][0]-1]
    print(wa)
    list[bc[i][1]-1] += list[bc[i][0]-1]
    list[bc[i][0]-1] = 0
