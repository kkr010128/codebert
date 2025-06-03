n = int(input())
ans = False
for i in range(1,10):
    if n%i==0 and 1<=(n//i)<=9:
        ans=True
        break
if ans:
    print('Yes')
else:
    print('No')
