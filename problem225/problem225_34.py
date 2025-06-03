H,A = map(int, input().split())

ans=0

for i in range(H//A+1):
    if H >0:
        H=H-A
        ans+=1
    else:
        break
print(ans)