n = int(input())
count = 0
ans = 'No'
for i in range(n):
    a , b = map(int,input().split(' '))
    if a!=b:
        count = 0 
    else:
        count += 1
    if count == 3:
        ans = 'Yes'
print(ans)