n=int(input())
s=input().split()
q=int(input())
t=input().split()
cnt=0

for i in range(q):
    for j in range(n):
        if s[j]==t[i]:
            cnt+=1
            break
            
print(cnt)
