n = int(input())
s = input()
ans = 0

for i in range(0,1000):
    num = str(i)
    if i < 10:
        num = "00"+num
    elif i <100:
        num = "0" + num
    f = 0
    for j in range(n):
        if s[j] == num[f]:
            f += 1
        if f == 3:
            break
    if f==3:
        ans +=1
print(ans)
                        
