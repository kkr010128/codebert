#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

a,b= map(int, input().split())


# xが１０円から１００００円まで

ans = -1

for i in range(10,10001):
    a1 = int(i*0.08)
    b1 = int(i*0.1)
    #print(a1,b1)
    if (a1 == a and b1 == b):
        ans = i
        break
print(ans)
