x,n = map(int,input().split())
p = list(map(int,input().split()))

i = 0
ans = -1

while True:
    temp1 = x - i
    temp2 = x + i
    if temp1 not in p:
        ans = temp1
        break
    if temp2 not in p:
        ans = temp2
        break
    i += 1
print(ans)