#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n = int(input())
p = list(map(int, input().split()))

ans = 1
minVal = p[0]

for i in range(1, n):
    if minVal > p[i]:
        ans += 1
        minVal = p[i]
print(ans)




