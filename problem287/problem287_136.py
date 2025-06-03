N = int(input())

ans = 'No'
if N<=82:
    for i in range(1,10):
        if N%i==0 and len(str(N//i))==1:
            ans = 'Yes'

print(ans)
