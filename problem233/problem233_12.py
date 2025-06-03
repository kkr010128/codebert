N = int(input())
li = list(map(int, input().split()))
an = 1
mi = li[0]
for i in range(1,N):
    if mi >= li[i]:
        an += 1
        mi = li[i]
print(an)