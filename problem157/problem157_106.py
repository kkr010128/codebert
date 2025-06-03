N = int(input())
As = list(map(int,input().split()))
dic = {}
array = []
x = As[0]
init = 1 - x
for i in range(1,N):
    v = init + i - 1 - As[i]
    array.append(v)
    if v not in dic:
        dic[v] = 1
    else:
        dic[v] += 1
if 0 in dic:
    ans = dic[0]
else:
    ans = 0

for i in range(1,N):
    y = As[i] + i - x
    z = array[i-1]
    dic[z] -= 1
    if y in dic:
        ans += dic[y]
print(ans)
