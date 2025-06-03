k = int(input())
cnt = 0
mod = [0]
not_found = 1
while cnt<k+1:
    cnt+=1
    n = mod[-1]*10+7
    mod.append(n%k)
    if n % k == 0:
        not_found = 0
        print(cnt)
        break
if(not_found):
    print(-1)
