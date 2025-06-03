s = int(input())
m = 10**9+7
a = [1,0,0,1,1,1,2]
if s < 7:
    print(a[s])
    exit()

for i in range(7,s+1):
    a.append((sum(a[3:i-2])+1)%m)

print(a[s])