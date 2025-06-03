a = [list(map(int, input().split())) for _ in range(3)]
N=int(input())
b = [int(input()) for _ in range(N)]


cnt=0

for i in range(N):
    for j in range(3):
        for k in range(3):
            if b[i] == a[j][k]:
                a[j][k] =1000
                if sum(a[j]) ==3000 or a[0][k]+a[1][k]+a[2][k]==3000 or a[0][0]+a[1][1]+a[2][2]==3000 or a[0][2]+a[1][1]+a[2][0]==3000:
                    cnt +=1
print('Yes' if cnt>0 else 'No')