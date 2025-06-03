N = int(input())
ans = 'No'
count =0
for i in range(N):
    d1,d2 = list(map(int,input().split()))
    if d1!=d2:
        count =0
    else:
        count +=1
    if count == 3:
        ans = 'Yes'
        break
print(ans)