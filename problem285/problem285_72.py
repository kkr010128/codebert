S = input()
N = len(S)

ans = 0
i = 0
while i < N and S[i]=='>':
    i += 1
ans += i*(i+1)//2

arr = [i]
while i < N:
    while i < N and S[i]=='<':
        i += 1
    arr.append(i)
    if i==N: break
    while i < N and S[i]=='>':
        i += 1
    arr.append(i)

arr = [b-a for a,b in zip(arr,arr[1:])]
for a,b in zip(arr[::2],arr[1::2]):
    if a<b: a,b = b,a
    ans += a*(a+1)//2
    ans += b*(b-1)//2
if len(arr)%2:
    ans += arr[-1]*(arr[-1]+1)//2

print(ans)