from collections import deque
[N,M] = list(map(int,input().split()))
AB = []
for i in range(M):
    AB.append(list(map(int,input().split())))

#そこから直で行けるところをまとめる
ikeru = [[] for i in range(N)]
for i in range(M):
    ikeru[AB[i][0]-1].append(AB[i][1]-1)
    ikeru[AB[i][1]-1].append(AB[i][0]-1)
# print('ikeru:',ikeru)



que = deque([])
que.append(0)
# print('que ini:',que)
out=[10**6]*N
out[0]=0

while que:
    p = que.popleft()
    # print('p,que:',p,que)

    for next in ikeru[p]:
        # print('next,out:',next,out)
        if out[next]==10**6:
            que.append(next)
            out[next]=p+1


# print(out)
print('Yes')
for i in range(1,N):
    print(out[i])

