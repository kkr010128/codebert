N,M = map(int,(input().split()))
s = list(input())
s.reverse()
now = 0
me = []
flag = 0

while now != N:
    for i in range(1,M+1,)[::-1]:
        if now + i <= N  and  s[now+i] == "0":
            now += i
            me.append(i)
            break
    else:
        print(-1)
        flag = 1
        break

if flag == 0:
    me.reverse()
    print(*me)