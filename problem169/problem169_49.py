n = int(input())
a = map(int,input().split())

boss = [[] for _ in range(n)]

for i,j in enumerate(a):
    boss[j-1].append(i)

for i in boss:
    print(len(i))