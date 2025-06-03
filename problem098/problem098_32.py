n = int(input())
c = input()
cnt = 0
ans = 0
for i in range(n):
    if(c[i]=='R'):
        cnt+=1
for i in range(cnt):
    if(c[i]=='W'):
        ans+=1
print(ans)