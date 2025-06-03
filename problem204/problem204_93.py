S = list(input())
N = int(input())
normalFlag = True
front = []
back = []
for _ in range(N):
    q = list(map(str,input().split()))
    if q[0] == '1':
        normalFlag = not normalFlag
    else:
        if q[1] == '1':
            if normalFlag:
                front.append(q[2])
            else:
                back.append(q[2])
        else:
            if normalFlag:
                back.append(q[2])
            else:
                front.append(q[2])

if normalFlag:
    front.reverse()
    ans = front+S+back
else:
    back.reverse()
    S.reverse()
    ans = back+S+front
print(''.join(map(str,ans)))