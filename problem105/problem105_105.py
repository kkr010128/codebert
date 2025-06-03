v = int(input())
n = list(map(int, input().split(' ')))
c = 0
for i in range(0, v, 2):
    if n[i] %2 == 1:
        #print(n[i])
        c += 1
print(c)
