#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))

n, k = map(int, input().split())

temp = [0] * n
for i in range(k):
    d = int(input())
    l = list(map(int, input().split()))
    for j in l:
        temp[j-1] += 1


ans = 0
for i in temp:
    if (i == 0):
        ans += 1

print (ans)

