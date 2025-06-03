from collections import deque

k = int(input())
cnt = 9
q = deque([])
for i in range(1,10):
    q.append(i)
ans = 0

if k < 10:
    print(k)
else:
    while cnt != k:
        n = q.popleft()
        if n%10 == 0:
            tmp = n*10
            q.append(n*10)
            cnt += 1
            if cnt == k:
                print(tmp)
                break
            q.append(1+tmp)
            cnt += 1
            if cnt == k:
                print(tmp+1)
                break
        elif n%10 == 9:
            tmp = n*10
            q.append(tmp+8)
            cnt+=1
            if cnt == k:
                print(tmp+8)
                break
            q.append(tmp+9)
            cnt += 1
            if cnt == k:
                print(tmp+9)
                break
        else:
            tmp = n%10
            q.append(tmp-1+(n*10))
            cnt += 1
            if cnt ==k:
                print(tmp-1+(n*10))
                break
            q.append(tmp+(n*10))
            cnt +=1
            if cnt == k:
                print(tmp+(n*10))
                break
            q.append(tmp+1+(n*10))
            cnt += 1
            if cnt == k:
                print(tmp+1+(n*10))
                break
