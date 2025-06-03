#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

x,n = map(int, input().split())
p = list(map(int, input().split()))

ans = x
for i in range(x, 102):
    if i not in p:
        ans = i
        break

ans2 = x
for i in range(x-1, -1, -1):
    if i not in p:
        ans2 = i
        break

#print(ans,ans2)
tmp1 = abs(ans - x)
tmp2 = abs(x - ans2)

if (tmp1 < tmp2):
    print(ans)
elif (tmp1 == tmp2):
    print(min(ans, ans2))
else:
    print(ans2)



