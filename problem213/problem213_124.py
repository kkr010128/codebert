#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n = int(input())
x = list(map(int, input().split()))

mix_x = min(x)
max_x = max(x)

ans = 10000000000000
for i in range(mix_x, max_x+1):
    power = 0
    for j in range(n):
        power += (x[j] - i)**2
    ans = min(ans, power)
print(ans)



