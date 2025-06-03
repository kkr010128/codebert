n = int(input())
d1 = [0] * n
d2 = [0] * n
for i in range(n):
    d1[i], d2[i] = map(int,input().split())

for i in range(n-2):
    if d1[i] == d2[i] and d1[i+1] == d2[i+1] and d1[i+2] == d2[i+2]:
        print('Yes')
        break
else:
    print('No')