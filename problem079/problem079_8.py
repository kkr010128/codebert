s = int(input())
m = 10**9+7
a = [1,0,0,1]
if s < 4:
    print(a[s])
    exit()

for i in range(4,s+1):
    a.append((a[3]+a[1])%m)
    a.pop(0)

print(a[3])