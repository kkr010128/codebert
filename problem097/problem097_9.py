K =  int(input())

a = [0]*1000001
ans = -1
a[1] = 7%K

for i in range(2,K+1):
    a[i] = (10*a[i-1]+7)%K
for i in range(1,K+1):
    if a[i] == 0:
        ans = i
        print(i)
        break
if ans == -1:
    print(-1)
