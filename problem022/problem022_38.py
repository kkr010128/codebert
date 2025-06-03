n = int(input())
s = list(map(int,input().split()))
q = int(input())
r = list(map(int,input().split()))
cou = 0

for i in range(q):
    for j in range(n):
        if(s[j] == r[i]):
            cou += 1
            break
print(cou)
