n = int(input())
a = list(map(int, input().split()))

dic = {}
ans = ''
for i in range(n):
    dic[a[i]] = i+1

for i in range(n):
    ans = ans + str(dic[i+1]) + ' '

print(ans)