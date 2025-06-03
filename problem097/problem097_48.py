k = int(input())
a = 7%k
flag = False
for i in range(k):
    if a == 0:
        flag = True
        ans = i+1
        break
    a = (10*a+7)%k
if flag:
    print(ans)
else:
    print(-1)