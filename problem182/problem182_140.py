n,k,c = map(int,input().split())
s = input()
canwork=[0]*(n+1) #canwork[i]:=i日目までに働くことができる最大日数(1-indexed)
canwork2 = [0]*(c+n+3)
for i in range(n):
    if s[i] == "o":
        canwork[i+1]=max(canwork[i],canwork[i-c]+1)
        
    else:
        canwork[i+1] = canwork[i]
        
for i in range(n)[::-1]:
    if s[i] == "o":
        canwork2[i]=max(canwork2[i+1],canwork2[i+c+1]+1)
    else:
        canwork2[i] = canwork2[i+1]

ans = []
for i in range(n):
    if canwork[i]+canwork2[i+1]==k-1:
        ans.append(i+1)
print(*ans)