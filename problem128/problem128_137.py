x,n= map(int,input().split())
p = list(map(int,input().split()))
ans,i = 0,0

while True:
    if x-i not in p:
        ans = x-i
        break
    if x+i not in p:
        ans = x+i
        break
    i = i+1
    
print(ans)